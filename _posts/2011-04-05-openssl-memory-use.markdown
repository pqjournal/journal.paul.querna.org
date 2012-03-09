---
date: '2011-04-05 07:41:23'
layout: post
slug: openssl-memory-use
status: publish
title: OpenSSL memory use in Node.js
wordpress_id: '810'
---

Last Thursday I went to the Joyent office for [Node Office Hours](http://blog.nodejs.org/2011/03/23/office-hours/) -- I wanted to talk to [Isaac](http://blog.izs.me/) about running a [private NPM registry](https://github.com/isaacs/npm/blob/master/doc/registry.md).

Isaac answered my questions about private NPM registries, but [Matt Ranney](https://github.com/mranney) explained a more interesting problem. He was dialed into a conference call line for Node Office hours (he is currently living in Hawaii.)  Matt explained that he is using the new [TLS module in Node v0.4](http://nodejs.org/docs/v0.4/api/tls.html), and it was using **1 megabyte of memory per connection!** Using 1mb per connection made us think there must be something wrong in Node.js itself, so we wrote up a simple test case client and server.

The TLS server says "welcome" to a newly connected client, and then echos anything it receives back to the client:

    
{% highlight javascript %}
var tls = require('tls');
var fs = require('fs');

var options = {
  key: fs.readFileSync('test_key.pem'),
  cert: fs.readFileSync('test_cert.pem'),
};

tls.createServer(options, function (s) {
  s.write("welcome!\n");
  console.log('got client');
  s.pipe(s);
}).listen(8000);
console.log('127.0.0.1:8000');
{% endhighlight %}



The client spawns 200 connections, and writes 'hello' to the server every 5 seconds for each connection:

    
{% highlight javascript %}
var tls = require('tls');

function go() {
  var s = null;
  s = tls.connect(8000, '127.0.0.1', function() {
    setInterval(function() {
      s.write('hello\n');
    }, 5000);
  });  
};

var i;
for (i = 0; i<200; i++) {
  go();
}
{% endhighlight %}


Running the client and server on my laptop, the server used almost 200 megabytes of memory.   This meant the high memory usage per-connection is not just a problem with Matt's application, but something deeper in Node.js.

At this point the Linux users are trembling, unsure how to debug the issue. Luckily, I still use [Steve's operating system](http://en.wikipedia.org/wiki/Mac_OS_X), and I fired up [Instruments.app](http://en.wikipedia.org/wiki/Instruments_(application)) to start taking a look at the problem.



## Those Pesky Certificate Authority Certificates



Using the builtin _Allocations_ instrument, I was looking for how memory was being used.  I expected to just see a large blob of allocation being done inside [v8](http://code.google.com/p/v8/), since Instruments and DTrace that power it do not have visibility inside the VMs internals. Unexpectedly, it quickly became apparent our main use of memory was the `node::crypto::SecureContext::AddRootCerts` function.  After going back to the Javascript, we could see that for every new TLS connection being made, Node was re-parsing the list of root-certificate authorities from their string forms, into the `X509_STORE` object used by OpenSSL:
[![](http://journal.paul.querna.org/wp-content/uploads/2011/04/pre-fix.jpg)](http://journal.paul.querna.org/wp-content/uploads/2011/04/pre-fix.jpg)


Just by commenting out one line of Javascript, we were able to reduce memory usage by 20%, and increased the performance of the HTTPS server from 70 requests/second to 700 requests/second.

[Ryan](http://tinyclouds.org/) changed the Node crypto code to use a single global CA store for the default root certificates in [5c35dff41](https://github.com/joyent/node/commit/5c35dff4192b0e204ab4145b7f9dcdba6e76a93e
).  The current _fix is a hack_, the correct long term fix is to better use [SSL_new](http://www.openssl.org/docs/ssl/SSL_new.html) with a shared `SSL_CTX*`, but that will require a larger refactoring of `node_crypto.cc`.



## Zlib: Big Buffers "R" us


We thought after fixing the obvious bug in parsing the certificates, we might be done. We went back to the profiling in Instruments.app, and discovered memory usage still was over 500kb per connection:
[![](http://journal.paul.querna.org/wp-content/uploads/2011/04/compression.jpg)](http://journal.paul.querna.org/wp-content/uploads/2011/04/compression.jpg)

We dove into the OpenSSL codebase, and found that Zlib Compression is enabled by default, and there isn't an easy way to turn it off. The [documentation for SSL_COMP_add_compression_method](http://www.openssl.org/docs/ssl/SSL_COMP_add_compression_method.html
) says:



> Unlike the mechanisms to set a cipher list, there is no method available to restrict the list of compression method on a per connection basis.



Recent  versions of OpenSSL (>1.0.0) have added `SSL_OP_NO_COMPRESSION` that can be disable compression per-connection via [SSL_CTX_set_options](http://www.openssl.org/docs/ssl/SSL_CTX_set_options.html).  However, most Linux distributions are still using variations of OpenSSL 0.9.8, meaning this option isn't viable for most users.

As an alternative, it is possible to zero out the global list of all OpenSSL compression methods after initializing OpenSSL:

{% highlight c %}
void disable_openssl_compression() {
  STACK_OF(SSL_COMP)* comp_methods = SSL_COMP_get_compression_methods();
  sk_SSL_COMP_zero(comp_methods);
};
{% endhighlight %}


This is a _terrible hack_, but it enabled us to test the effect of disabling compression on the server side, and after seeing the results, I think it is worth it.

With this change, we ran the test again, and see an amazing thing, we are only using about 15 megabytes of memory, and we can actually see the v8 garbage collector doing work now:
[![](http://journal.paul.querna.org/wp-content/uploads/2011/04/all-fixed.jpg)](http://journal.paul.querna.org/wp-content/uploads/2011/04/all-fixed.jpg)



## Ship it to production


Going back to Matt's original problem, he is using Node.js as part of the server side infrastructure for [Voxer, a communication application for mobile devices](http://voxer.com/).  He applied the patches, and provided this graph from Cacti showing the massive improvement in free memory:

[![](http://journal.paul.querna.org/wp-content/uploads/2011/04/Cacti.png)](http://journal.paul.querna.org/wp-content/uploads/2011/04/Cacti.png)



## What about Twisted Python?


At [Rackspace/Cloudkick](https://www.cloudkick.com/) we use [Twisted Python](http://twistedmatrix.com/trac/) for many production services, including several with many thousands of open TLS connections.  We had always just assumed the high memory usage was an issue in Twisted Python itself, not something in OpenSSL.  We had tried looking at the memory usage using [Dowser](http://www.aminus.net/wiki/Dowser), but we never got far, as it always looked like Python wasn't misbehaving.  This now makes sense, because the OpenSSL objects used in [pyOpenSSL](http://packages.python.org/pyOpenSSL/) wouldn't be counted by Dowser.

pyOpenSSL is a limited binding of the most useful functions in OpenSSL, so it doesn't provide bindings to the functions that can manipulate the OpenSSL Compression settings. I decided to use the [ctypes module](http://docs.python.org/library/ctypes.html) to avoid needing to distribute a C based extension to disable OpenSSL compression:

{% highlight python %}
def disableSSLCompression(self):
  try:
    import ctypes
    import glob
    openssl = ctypes.CDLL(None, ctypes.RTLD_GLOBAL)
    try:
      f = openssl.SSL_COMP_get_compression_methods
    except AttributeError:
      ssllib = sorted(glob.glob("/usr/lib/libssl.so.*"))[0]
      openssl = ctypes.CDLL(ssllib, ctypes.RTLD_GLOBAL)

    openssl.SSL_COMP_get_compression_methods.restype = ctypes.c_void_p
    openssl.sk_zero.argtypes = [ctypes.c_void_p]
    openssl.sk_zero(openssl.SSL_COMP_get_compression_methods())
  except Exception, e:
    log.msg('disableSSLCompression: Failed:')
    log.msg(e)
{% endhighlight %}



We deployed this to one Twisted Python Service as a test, and you can see the impact on memory use, dropping form 1.15 gigabytes to around 300 megabytes:

[![](http://journal.paul.querna.org/wp-content/uploads/2011/04/twisted-memory.jpg)](http://journal.paul.querna.org/wp-content/uploads/2011/04/twisted-memory.jpg)



## Conclusion



While compression in TLS can be helpful in some situations with bulk data transfers, the method by which OpenSSL has done it is disappointing.  Enabling a feature by default that has such a large impact on memory usage, and not having a reasonable way to disable it is bad library design.

If you have specific applications using TLS that don't benefit from compression or have many thousands of mostly idle connections, consider disabling OpenSSL's compression methods to save yourself about 500kb of memory per connection.

**PS:** [agl on HN](http://news.ycombinator.com/item?id=2411349) mentioned that OpenSSL > 1.0.0 also has `SSL_MODE_RELEASE_BUFFERS` which greatly reduces memory usage of a connection -- this is [already done in Node.js if available](https://github.com/joyent/node/blob/v0.4.5/src/node_crypto.cc#L622-625), but if you are updating older code be sure to add this too.


