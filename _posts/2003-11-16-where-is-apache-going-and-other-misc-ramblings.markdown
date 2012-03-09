---
date: '2003-11-16 23:23:39'
layout: post
slug: where-is-apache-going-and-other-misc-ramblings
status: publish
title: Where is Apache going and other misc. ramblings.
wordpress_id: '13'
---

The Apache [HTTPd Devel Mailing list](http://marc.theaimsgroup.com/?l=apache-httpd-dev) has been on fire for the past couple days.  

Much of the discussion started out of the lack of major development for Apache 2.0, and the lack of overall deployment.  
  

Some how the idea of opening the 1.3 tree to increased development came up.  I think any attempt to increase the status of Apache 1.3 beyond maintance only is a very **bad** idea.  Doing that will only split an already small group of developers into two different camps.  
  


[Rasmus](http://lerdorf.com), the creator of [PHP](http://www.php.net) also made a comment:


Quote from Rasmus Lerdorf:

And a threaded mpm is just not an option.  Most humans
are simply not smart enough to write threadsafe code.  




Frankly, most humans are not programers. I think that threadsafe code is not that difficult to write, and the performance gains can be signifigant in Apache's case.  Maybe I am just angry at the PHP developers FUD about Apache 2  
  

Part of the problem I see in Apache Development is lack of a clear direction.  For example the [ROADMAP](http://cvs.apache.org/viewcvs.cgi/~checkout~/httpd-2.0/ROADMAP?rev=1.26&content-type=text/vnd.viewcvs-markup) file hasn't been updated in over 1 year.  What Apache needs is an updated plan on where to go from here.  Opening 1.3 up for development is not the solution to that.  

  
  

In other news, my [mod_authn_cache module](http://mod-auth.sf.net) is coming along well. [LDAP Cache](http://nagoya.apache.org/bugzilla/show_bug.cgi?id=18756) that I was basing the shared memory caching on is completely broken so I changed to the 
[SSL Hash Table Cache](http://nagoya.apache.org/bugzilla/show_bug.cgi?id=17876).  Has anyone made a bug free Shared memory Cache for Apache? If they have, [Google](http://www.google.com) hasn't helped me finding one.  
  



Quote from Justin Erenkrantz:


You win the lucky prize for the day.    Committed.  (Jeff and I went, 'Sure, looks fine.')



Also got a [Patch](http://force-elite.com/~chip/patches/apr-util/apr_md5/) to add SHA1 support to apr_password_validate applied. I feel special. I got the lucky prize for the day!  

  
Besides all the bullshit going on at dev@httpd today, everything was going fairly good untill i tried updating the [mod-auth website](http://mod-auth.sf.net/).  Of course the [SourceForge.net](http://www.sourceforge.net) Shell Servers are down, and there is no ETA. Welp that Sucks. I think I will just goto bed now.  

