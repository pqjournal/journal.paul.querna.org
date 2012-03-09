---
date: '2009-08-24 16:08:54'
layout: post
slug: downtime-page-in-apache
status: publish
title: downtime page in apache
wordpress_id: '312'
---

It is good practice to send 503 Status codes when your site has downtime  or is doing an upgrade.

The easiest way to do this for all your URLs is something like this using [mod_asis](http://httpd.apache.org/docs/trunk/mod/mod_asis.html):

    
           # Bind mod_asis to files ending in .asis
           AddHandler send-as-is asis
           # Add other Aliaes/AliasMatches for any other resources needed (logos, css, etc)
           Alias /logo.png /opt/mysite/maint/logo.png
           # The magic line, pulling all matching URLs into one file
           AliasMatch /(.*) /opt/mysite/maint/index.html.asis


Your index.html.asis would contain something like this:

    
    Status: 503
    Cache-Control: no-cache
    Content-type: text/html
    
    <html><h1>My site is down, be back soon!</h1></html>
    


I can't help you make a fail whale / [plumber image](http://www.flickr.com/photos/vista/2905439095/) though, that is up to you
