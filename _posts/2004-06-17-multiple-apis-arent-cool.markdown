---
date: '2004-06-17 23:01:35'
layout: post
slug: multiple-apis-arent-cool
status: publish
title: Multiple APIs aren't cool
wordpress_id: '21'
---

I spent time today porting some software from Linux to [FreeBSD](http://www.freebsd.org).
  
  

[Someone](http://www.darktones.com/) thought it would be cool to use [GUIDs](http://www.ics.uci.edu/~ejw/authoring/uuid-guid/draft-leach-uuids-guids-01.txt). Of course, the [FreeBSD implmentation](http://www.freebsd.org/cgi/man.cgi?query=uuid) is completely different from the [Linux implmentation](http://www.die.net/doc/linux/man/man3/libuuid.3.html). [Some people complain](http://www.joelonsoftware.com/articles/APIWar.html) about Microsoft changing their API.   
  

I would settle for the Open Source Operating systems having a more unified API. For example, why are there two different replacements for poll? (Linux: [sys_epoll](http://www.xmailserver.org/linux-patches/nio-improve.html) FreeBSD: [kqueue](http://www.freebsd.org/cgi/man.cgi?query=kqueue))  
  

Geez. Been a long time since I last posted. Maybe I should post more often.
