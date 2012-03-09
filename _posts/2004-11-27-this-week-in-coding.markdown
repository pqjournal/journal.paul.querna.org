---
date: '2004-11-27 17:11:23'
layout: post
slug: this-week-in-coding
status: publish
title: This Week in Coding
wordpress_id: '41'
---

  * APR: Added support for _apr_os_uuid_get()_ on Linux and FreeBSD.  Linux has a [uuid_generate](http://www.fifi.org/cgi-bin/man2html/usr/share/man/man3/uuid_generate_time.3.gz) as part of libuuid.  FreeBSD has [uuid_create](http://www.freebsd.org/cgi/man.cgi?query=uuid_create) as part of it's libC, and of course, they both have completely different schematics.  I first got to know the different interfaces when I ported the [Plasma Servers](http://plasma.cyanworlds.com/) to FreeBSD, since we use GUIDs in several places. [r106214](http://svn.apache.org/viewcvs?view=rev&rev=106214).
  
  


  * APR: Committed a first swing at support for Solaris 10's ['Event Completion Framework'](http://developers.sun.com/solaris/articles/event_completion.html).  Their interface is a little weird.  You must add a _file descriptor_ back into the Set after any event is done with it.  KQueue and EPoll on the other hand leave the _file descriptor_ in the Set until you explicitly remove it.  On a personal level, I prefer the KQueue and EPoll type interface, but the Solaris 10 one works, just with more system calls. [r106156](http://svn.apache.org/viewcvs?view=rev&rev=106156).
  
  


  * HTTPD: The Event MPM.  This patch has been in various incarnations since mid-July.  I actually did most of the coding in August on a road trip to Seattle for a [Mariners Game](http://seattle.mariners.mlb.com/). The patch came in at over 160k, mostly because large portions of the code where copied from the [Worker MPM](http://httpd.apache.org/docs-2.1/mod/worker.html). [r105919](http://svn.apache.org/viewcvs?view=rev&rev=105919).
  
  


It was a busy week!
