---
date: '2005-03-06 16:46:42'
layout: post
slug: eat-your-own-dog-food
status: publish
title: Eat Your Own Dog Food
wordpress_id: '56'
---

This site is now running off the [Event MPM](http://httpd.apache.org/docs-2.1/mod/event.html), that I helped write.  
  

I still have several sites that require PHP, so I am using [mod_fcgid](http://fastcgi.coremail.cn/) to run all of the remaining PHP Scripts via FastCGI.  
  

Only the [Until Uru Signup page](http://con.plasma.corelands.com/) had issues after the upgrade.  This page was using the `apache_add_output_filter` function added by [my apache2-filters patch for PHP](http://www.in.force-elite.com/~chip/patches/php-src/apache2-filters/).  Since the PHP was no longer running inside apache, this function did not exist. The Until Uru templates are all built in XSLT, and the PHP was adding a [XSLT Output Filter](http://www.outoforder.cc/projects/apache/mod_transform/) to process the XML it generates. To fix this, I modified the script send an extra header:


Quote from header.php:


    header("Content-Type: application/needs-xslt");


I then told `mod_transform` to act on this:


Quote from httpd.conf:


    AddOutputFilterByType XSLT application/needs-xslt


It seems everything else is working great.  If anything is broken, please let me know.

