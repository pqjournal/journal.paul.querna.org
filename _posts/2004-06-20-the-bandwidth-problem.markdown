---
date: '2004-06-20 23:56:26'
layout: post
slug: the-bandwidth-problem
status: publish
title: The Bandwidth Problem
wordpress_id: '24'
---

Most shared hosting systems want some sort of system to prevent a few hosts from using all the available bandwidth. I have been rather disappointed by my choices.  
  

For Apache 1.3.XX there are many options:


  * [mod_throttle](http://www.snert.com/Software/mod_throttle/) (Semi-Public Domain License) - Shared Mem based (good!). Active Development.

  * [mod_bandwidth](http://www.cohprog.com/mod_bandwidth.html) (Apache License) - File Based in /tmp (BAD). Inactive Development.

  * [mod_bwshare](http://www.topology.org/src/bwshare/README.html) (Artistic License) - Shared Memory based (good!). Inactive Development.

  * OS Based: [Netfilter - Linux](http://www.netfilter.org/) (GPL License) - In Kernel (good!). Active Development. (1) 

  * OS Based: [FreeBSD - ALTQ](http://pf4freebsd.love2party.net/altq.html) (BSD License) - In Kernel (good!). Active Development. (1)


For Apache 2.0.XX:

  * [mod_bwshare](http://www.topology.org/src/bwshare/README.html) (Artistic License) - Shared Memory based (good!). Inactive Development.

  * OS Based: [Netfilter - Linux](http://www.netfilter.org/) (GPL License) - In Kernel (good!). Active Development. (1) 

  * OS Based: [FreeBSD - ALTQ](http://pf4freebsd.love2party.net/altq.html) (BSD License) - In Kernel (good!). Active Development. (1)


(1) Not easy todo filtering based on filetype/vhost/http specific things.  
  


Ah. Only mod_bwshare for Apache 2.0. And its not actively supported by its author for Apache 2.0.  Not a good situation at all.  It seems to *work* with Apache 2, but I do not like modules that have been abandoned by their authors.  
  

Personaly, I would prefer an OS level bandwidth shapping, but these do not allow the type of configurations that most shared hosting companies want.
