---
date: '2005-04-07 01:08:46'
layout: post
slug: tcp_cork-is-good-for-your-server
status: publish
title: TCP_CORK is good for your server
wordpress_id: '66'
---

Christopher Baus has a [great article on TCP_CORK](http://www.baus.net/on-tcp_cork).  
  

Hopefully this weekend I can do some tcpdump action on apache, and look at how much packet fragmentation there is, since Apache does not use TCP_CORK, but instead it only uses [TCP_NODELAY](http://www.unixguide.net/network/socketfaq/2.16.shtml), which can result in non-optimal conditions if you do many small write()s.
