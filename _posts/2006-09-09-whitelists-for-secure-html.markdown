---
date: '2006-09-09 00:46:39'
layout: post
slug: whitelists-for-secure-html
status: publish
title: whitelists for secure HTML
wordpress_id: '162'
---


[Microsoft's RSS Team comments](http://blogs.msdn.com/rssteam/archive/2006/09/09/747111.aspx) on all the [security stuff](http://www.snellspace.com/wp/?p=448):




> 
**Sanitization**: First, the Windows RSS Platform uses several techniques to strip out script (and several other variations of malicious HTML) before storing the feed content.





Great, except, uhm, its a horrible plan. The only way to really sanitize HTML input is to rebuild it into a DOM, and [apply a whitelist of allowed HTML tags and attributes](http://www.feedparser.org/docs/html-sanitization.html).  Once that is done, re-render the DOM. [All 'strip' techniques will fail](http://ha.ckers.org/xss.html), sooner or later.

