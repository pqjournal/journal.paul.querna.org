---
date: '2005-03-31 02:50:42'
layout: post
slug: lt-limit-gt-is-a-bad-idea
status: publish
title: Limit is a bad idea
wordpress_id: '64'
---

Trying to help someone on IRC today.. their existing .htaccess file was very scary.  It used the [&lt;Limit&gt;](http://httpd.apache.org/docs-2.1/mod/core.html#limit) directive, in completely the wrong context:


Quote from from a .htaccess file:



    
    
    <Limit GET POST>
        require valid-user
    </limit>
    





This means that any other HTTP method could access the site without **any** authentication.  The kicker is that mod_php will allow **any** HTTP method.  It doesn't just restrict to GET or POST requests.   
  

Apache by itself only by default allows GET and HEAD requests on static files.  Anyways, let this be a warning, when you think you need [&lt;Limit&gt;](http://httpd.apache.org/docs-2.1/mod/core.html#limit), you probally don't.  Ever. Really. I am Serious. Do not use 'Limit'.  
  


Most people really want [&lt;LimitExcept&gt;](http://httpd.apache.org/docs-2.1/mod/core.html#limitexcept). But, I believe that in most cases, you should avoid optional authentication.  I think that authentication should be required for an entire path, and not optional, depending on how the client munges the request.  Optional Client Certs are also a bastard to get working too, so the best solution is to just avoid the entire 'optional' authentication mindset.
