---
date: '2005-09-25 19:53:27'
layout: post
slug: need-beta-testers
status: publish
title: Need Beta Testers
wordpress_id: '102'
---


Okay, so I don't have a cool form [embedded into this blog entry](http://blakeross.com/index.php?p=170) asking for your email address to get sent an email message about a super-secret and revolutionary Web 3.0 product, BUT, I really do need people to help testing.



Apache HTTPD 2.1.8-BETA is [available for testing](http://people.apache.org/~pquerna/dev/httpd-2.1.8/).  I would love feedback, both positive and negative.  Please install it on your production servers, see what breaks. It wouldn't hurt to  try [some of the new features](http://httpd.apache.org/docs/2.1/new_features_2_2.html) too.



One of the coolest features that was just recently added is [graceful-stop](http://httpd.apache.org/docs/2.1/stopping.html#gracefulstop).  This allows you to drain connections to your web server, and do an upgrade without any downtime.  Thanks to [Colm](http://www.stdlib.net/~colmmacc/) for adding it.



Full ChangeLog: [CHANGES_2.1](http://people.apache.org/~pquerna/dev/httpd-2.1.8/CHANGES_2.1)

