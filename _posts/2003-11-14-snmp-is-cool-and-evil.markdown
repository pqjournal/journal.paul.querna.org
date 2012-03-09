---
date: '2003-11-14 21:07:16'
layout: post
slug: snmp-is-cool-and-evil
status: publish
title: SNMP is cool and evil.
wordpress_id: '11'
---

Earlier today I started on a tool to monitor the schools 100 odd printers.  They want to keep track of toner ussage and maintance on all the printers.  After some hacking around with the [Printer MIB RFC](http://www.faqs.org/rfcs/rfc1759.html) I was able to get the toner levels from all the HP printers on campus.  I still haven't got the Lexmarks reporting properly.  

  

Now, I think its totaly cool to have all the Info that SNMP can provide.  For example I use it with [MRTG](http://people.ee.ethz.ch/~oetiker/webtools/mrtg/) for the box in my dorm room.  But SNMP sucks.  Seriously.  OIDs seem like a good idea at first, and its cool that companies can easily extend them, but god damn they are a PITA to work with.  

  

Hey, but my PHP based printer monitor should be cool once its all done :)
