---
date: '2005-12-30 19:26:00'
layout: post
slug: native-fastcgi-is-coming
status: publish
title: native FastCGI is coming
wordpress_id: '119'
---


So, the [Ruby on Rails people are getting excited](http://weblog.rubyonrails.com/articles/2005/12/29/apache-gets-serious-about-fastcgi#comments) about Apache HTTPD getting native FastCGI support.



To prove that [mod_proxy_fcgi](http://svn.apache.org/repos/asf/httpd/httpd/branches/fcgi-proxy-dev/modules/proxy/mod_proxy_fcgi.c) isn't vaporware, I [present a live/running demo](http://paul.querna.org/fcgi-test/).



And here is how its configured:



    ProxyPass /fcgi-test fcgi-tcp://127.0.0.1:9500/



And here is the source code:


    import cgi
    import types

    def myapp(environ, start_response):
        start_response('200 OK', [('Content-Type', 'text/html')])
        out = ""
        # Print all environment variables
        out = out+"<h3>mod_proxy_fcgi test page</h3>"
        out = out+"<dl>"
        env_keys = environ.keys()
        env_keys.sort()
        for e in env_keys:
            if (type(environ[e]) == types.StringType):
              out = out+"<dt>"+cgi.escape(e+'='+'"'+environ[e]+'"') + "</dt>"
        out = out+"</dl>"
        return out

    if __name__ == '__main__':
        from flup.server.fcgi import WSGIServer
    #    from flup.server.ajp import WSGIServer
        WSGIServer(myapp, bindAddress=("127.0.0.1",9500)).run() 




Most of the credit really should go to [Garrett](http://asdf.blogs.com/asdf/).  He has been writing most of the actual code.  I have just been watching the Firefly DVDs and inserting sneer comments about how XYZ patch doesn't work with XYZ library.



Finally, A shout out to the [Flup library](http://www.saddi.com/software/flup/) for python.  It supports AJP, FastCGI and SCGI, making it much easier to move applications between all the available connector protocols.
  

  
**Update: **Okay, like any new code there are bugs.  The test page isn't working right now..... Oh well.

