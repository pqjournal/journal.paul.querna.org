---
date: '2005-04-06 02:23:27'
layout: post
slug: the-long-road-of-development
status: publish
title: The long road of development....
wordpress_id: '65'
---

I released [mod_gnutls](http://www.outoforder.cc/projects/apache/mod_gnutls/) today.  I started hacking on the idea in August 2004, more than 7 months ago.  This is the longest any of my open source modules have been under development without a release.

  
  

mod_gnutls is an alternative to mod_ssl.  mod_ssl is a giant beast of a module -- no offense to it's authors is intended -- but I believe it has fallen prey to massive feature bloat.
  
  

When I started hacking on httpd, mod_ssl remained a great mystery to me, and when I actually looked at it, I ran away.  The shear ammount code is depressing, and it does not conform to the style guidelines.  It was painful to read, and even harder to debug.  I wanted to understand how it worked, and I had recently heard about GnuTLS, so long story short, I decided to write mod_gnutls.
  
  

Lines of Code in mod_ssl: 15,324  

Lines of Code in mod_gnutls: **1,886**  

  

One of the unique features is support for a distributed SSL Session Cache using [memcached](http://www.danga.com/memcached/). If anyone has a cluster of HTTPS servers, and would like a performance boost, I would love some test results.
  

  

Right now its not quite a viable alternative to mod_ssl -- it mostly needs testing and some serious code reviews.  I plan to add full support for SSL Client Certificates in the next version.  
  

I am pretty sure I will release a 0.1.1 in the next week that can compile on the 2.0.x branch.  There are a few function renames that force the current 0.1.0 release to require the 2.1.x-dev branch.  
  

It only took 7 months of hacking, but I am happy with the results so far.  mod_gnutls forced me to truely learn about input and output filters like never before.  The best way to really understand something is to write it from scratch -- and the result is that I now understand mod_ssl and GnuTLS better than before.
