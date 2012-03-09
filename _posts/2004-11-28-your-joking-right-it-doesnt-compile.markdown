---
date: '2004-11-28 20:44:47'
layout: post
slug: your-joking-right-it-doesnt-compile
status: publish
title: Your Joking right? it doesn't compile?
wordpress_id: '42'
---

For the first time in my recent memory, the [httpd](http://httpd.apache.org/) development branch would [not compile](http://marc.theaimsgroup.com/?l=apache-httpd-dev&m=110159777324460&w=2)!  It turned out to be some old functions were not exported properly, and this caused undefined symbols on some platforms.  Is a broken build a sign of progress for a project that has been idle?  Is this the starting of a new life?  
  

On the [httpd frontpage](http://httpd.apache.org/) there is now a link to the [2.1/2.2 Documentation](http://httpd.apache.org/docs-2.1/).  The next step is get a _2.1-alpha_ release on there.  Hopefully that will get done this week, since [PCRE 5.0](http://www.pcre.org/) has been merged in.  
  

I also knocked off an [old bug](http://issues.apache.org/bugzilla/show_bug.cgi?id=25718) in APR where it was trying to do runtime detection of [sendfile](http://www.freebsd.org/cgi/man.cgi?query=sendfile&sektion=2) support on FreeBSD. [r106850](http://svn.apache.org/viewcvs?view=rev&rev=106850)
