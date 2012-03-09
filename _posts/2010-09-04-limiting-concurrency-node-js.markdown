---
date: '2010-09-04 20:17:10'
layout: post
slug: limiting-concurrency-node-js
status: publish
title: Limiting Concurrency in Node.js
wordpress_id: '522'
tags:
- node.js
---

Lets say you are writing your new awesome web application in Node.js, because you know, Node.js is the new hotness and awesome.

Lets also say, your new Node.js web application does non-trivial things, and hits a limited backend resource. You can't rewrite this backend system in the new hotness of async Node.js yet, so it can only handle 10 concurrent clients. This should be a very common situation unless you happen to be at a new startup and are green fielding your entire application stack. If thats your case, Lucky you! But for everyone else, you need to control the amount of concurrency that Node.js applies to your backend.

I am going to examine the simplest case of an HTTP server, which hits a backend resource, transforms it, and returns it to the client. Oh yeah, I mean a Reverse Proxy server; A Proxy server isn't all that different from most application servers, taking client input and hitting different backends.  A proxy server just happens to hit HTTP most of the time, while an application server hits a database or another resource, but lets not get too deep into that. Node.js just happens to make writing proxy servers very easy, and relatively short, so I like using it as an example.

All of the source code for the examples can be found inside [my node-examples repository on github](http://github.com/pquerna/node-examples/tree/master/limiting_concurrency).



## Basic Reverse Proxy



Here is our simple application server in Node.js, it takes in a client request, and proxies it to http://nodejs.org/, [server_nolimit.js](http://github.com/pquerna/node-examples/blob/master/limiting_concurrency/server_nolimit.js):

{% highlight javascript %}
var http = require('http');
var sys = require('sys');
var destination = "nodejs.org";

http.createServer(function(req, res) {
  var proxy = http.createClient(80, destination);
  var preq = proxy.request(req.method, req.url, req.headers);

  console.log(req.connection.remoteAddress +" "+ req.method +" "+req.url);
  preq.on('response', function(pres) {
    res.writeHead(pres.statusCode, pres.headers);
    sys.pump(pres, res);
    pres.on('end', function() {
      preq.end();
      res.end();
    });
  });
  req.on('data', function(chunk) {
    preq.write(chunk, 'binary');
  });
  req.on('end', function() {
    preq.end();
  });
}).listen(8080);</code>
{% endhighlight %}


Note, this is in no way a valid HTTP 1.1 Proxy server, it breaks all kinds of things in the RFC, but its just bad enough for demos to work.  It takes a client request in, creates an outgoing HTTP client request, and uses `sys.pump` to transfer the data.

It is functional, and if you threw 1000 concurrent clients at it, it would want to open 1000 connections to nodejs.org. Poor nodejs.org!



## Limiting Outgoing Connections



This might appear to be the simplest approach, keep a count of the active clients, and if we are over the limit, start queuing any new clients.

The problem comes in with how Node.js behaves;  You will also need to buffer any incoming data while the request is queuing.  You could try to call `pause()` on the stream, but this is only advisory, so streams can still trickle some data you need to buffer.  This means our simple code of adding a counter, becomes complicated by extra buffering and work arounds for how Node's HTTP streams work.

[server_limit_clients.js implements this](http://github.com/pquerna/node-examples/blob/master/limiting_concurrency/server_limit_client.js), it accepts the client request, and keeps a currentClients variable up to date with the number of active outgoing requests.  When one request finishes, it starts processing the next one:

{% highlight javascript %}
var http = require('http');
var sys = require('sys');
var destination = "nodejs.org";

var maxClients = 1;
var currentClients = 0;
var _pending = [];

function process_pending()
{
  if (_pending.length > 0) {
    var cb = _pending.shift();
    currentClients++;
    cb(function() {
      currentClients--;
      process.nextTick(process_pending);
    });
  }
}

function client_limit(cb, req, res) 
{
  if (currentClients < maxClients) {
    currentClients++;
    cb(function() {
      currentClients--;
      process.nextTick(process_pending);
    }, req, res);
  }
  else {
    console.log('Overloaded, queuing clients...');
    _pending.push(cb);
  }
}

http.createServer(function(req, res) {
  var bufs = [];
  var done_buffering = false;

  client_limit(function(done){
    var proxy = http.createClient(80, destination);
    var preq = proxy.request(req.method, req.url, req.headers);

    console.log(req.connection.remoteAddress +" "+ req.method +" "+req.url);
    preq.on('response', function(pres) {
      res.writeHead(pres.statusCode, pres.headers);
      sys.pump(pres, res);
      pres.on('end', function() {
        preq.end();
        res.end();
        done();
      });
    });

    function finishreq() {
      bufs.forEach(function(buf){
        preq.write(buf);
      });
      preq.end();
    }

    if (done_buffering) {
      finishreq();
    }
    else {
      req.on('end', function() {
        finishreq();
      });
    }
  });

  req.on('data', function(chunk) {
    var tbuf = new Buffer(chunk.length);
    chunk.copy(tbuf, 0, 0);
    bufs.push(tbuf);
  });

  req.on('end', function() {
    done_buffering = true;
  });

}).listen(8080);</code>
{% endhighlight %}


**I have to say, ew!** It just got too complicated.  This buffering yourself stuff sucks.  In addition, if you had 1000 clients connect, most clients would just see a wonderful spinning spinner on their browser, waiting for their turn to get an outgoing client.



## Limiting by accepting less



If your Node.js application is deployed behind a load balancer of some kind, it might be a better idea to provide it with back pressure to your load balancer, so it sends your application less traffic.  A simple way to achieve this is to stop listening for connections.

When a socket in TCP is set to [listen for incoming connections](http://www.freebsd.org/cgi/man.cgi?query=listen), the kernel keeps a backlog of pending connections, so while this method isn't perfect, under high load it will quickly push back to your load balancer to stop sending your application traffic.  One problem is that currently Node.js hard codes 128 connections in the TCP listener backlog, so if your desired concurrency level is very low, this method will not be very effective in applying back pressure.

In addition because of how Node.js' `IOWatchers` work, even if you tell it to stop listening, it will continue processing any sockets it has already called accept on, meaning that this method is very crude, and relatively inaccurate on having exactly X clients making backend requests.

[server_limit_incoming.js implements this](http://github.com/pquerna/node-examples/blob/master/limiting_concurrency/server_limit_incoming.js), it reads new client requests until there are too many inflight, then it calls an internal function on the server instance's watcher object, `stop()`.  This stops libev from listening for new clients on that socket, it removes it from the event loop.  Once we are back below the maximum clients, it calls start on the IOWatcher, which adds the listening socket back to the event loop:

{% highlight javascript %}
var http = require('http');
var sys = require('sys');
var destination = "nodejs.org";
var port = 8080;
var maxClients = 2;
var currentClients = 0;
var active = true;

var hs = null;

function activate() {
  if (!active && currentClients < maxClients) {
    hs.watcher.start();
    active = true;
  }
}

hs = http.createServer(function(req, res) {
  var proxy = http.createClient(80, destination);
  var preq = proxy.request(req.method, req.url, req.headers);

  console.log(req.connection.remoteAddress +" "+ req.method +" "+req.url);
  preq.on('response', function(pres) {
    res.writeHead(pres.statusCode, pres.headers);
    sys.pump(pres, res);
    pres.on('end', function() {
      preq.end();
      res.end();
      currentClients--;
      activate();
    });
  });
  req.on('data', function(chunk) {
    preq.write(chunk, 'binary');
  });
  req.on('end', function() {
    preq.end();
  });

  currentClients++;
  if (currentClients >= maxClients) {
    hs.watcher.stop();
    active = false;
  }
});

hs.listen(port);

{% endhighlight %}



Overall this approach of stop accepting new clients is far less code than the earlier limiting method, and it lets your load balancers do smarter things under high load, hopefully meaning you have extra capacity on another machine, rather than just accepting more clients on an already overloaded server.  It does use some 'hacky' knowledge internals of how HTTP streams and IO Watchers work inside Node.js, and it is far less accurate in its counting. However, I believe that this method is probably one of the better ways to limit your concurrency inside Node.js.
