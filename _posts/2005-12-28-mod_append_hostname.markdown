---
date: '2005-12-28 14:22:18'
layout: post
slug: mod_append_hostname
status: publish
title: mod_append_hostname
wordpress_id: '117'
---


[mod_append_hostname](http://people.apache.org/~pquerna/modules/mod_append_hostname-0.1.0.tar.bz2) is a very simple Apache 2.x filter module.  It appends the [hostname](http://www.freebsd.org/cgi/man.cgi?query=gethostname) of the current machine, in an HTML comment, at the bottom of HTML content types:


> 
<!-- water-wireless.in.force-elite.com -->



Configuration:


> 
LoadModule append_hostname_module modules/mod_append_hostname.so
  

  
AddOutputFilterByType append_hostname text/html



Very useful when one of your machines behind a load balancer is kinda broken. Based on the an example from [Hacking Apache HTTP Server at Yahoo!](http://public.yahoo.com/~radwin/).  I actually wrote it an hour after the session, at [ApacheCon US 2005](http://apachecon.com/2005/US/index), but I haven't had a chance to post anything about it.

