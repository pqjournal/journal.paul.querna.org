---
date: '2008-11-30 23:47:14'
layout: post
slug: progress-on-apache-24
status: publish
title: progress on apache 2.4
wordpress_id: '247'
---

My [todo list](http://journal.paul.querna.org/articles/2008/11/26/todo/) from before thanksgiving:


> 

> 
> 
	
>   * Improve the Simple MPM.
> 
	
>   * Integrate Lua and mod_wombat into httpd trunk.
> 
	
>   * Improve the FastCGI Support in httpd turnk.
> 
	
>   * Finish my little infrastructure stats & graphs project.
> 




Well, I did get something working on my Infrastructure Stats Project.  You can see the [work in progress here](http://www.apache.org/dev/stats/).  It uses [flot](http://code.google.com/p/flot/) and [jquery](http://jquery.com/) to draw graphs of the mail and code commits at the ASF since the Apache Project started in 1996.

I didn't get around to most of my httpd goals, since every time I work on the Simple MPM, the fact that KQueue causes a kernel panic on OSX kinda discourages me.  I was hoping that the latest kernels from Apple would fix the problem, but they don't.

I did manage to commit 4 new modules to httpd trunk however:



	
  * [mod_heartbeat](https://svn.apache.org/repos/asf/httpd/httpd/trunk/modules/cluster/README.heartbeat) - Generates [Multicast](http://en.wikipedia.org/wiki/Multicast) heartbeat messages containing the status of the server.

	
  * [mod_heartmonitor](https://svn.apache.org/repos/asf/httpd/httpd/trunk/modules/cluster/README.heartmonitor) - Collects these Multicast heartbeats for other modules to use.

	
  * [mod_ratelimit](https://svn.apache.org/repos/asf/httpd/httpd/trunk/modules/filters/mod_ratelimit.c) - Bandwidth Rate Limiting for Clients.

	
  * [mod_lbmethod_heartbeat](https://svn.apache.org/repos/asf/httpd/httpd/trunk/modules/proxy/mod_lbmethod_heartbeat.c) - Module to [Load Balance mod_proxy_balancer workers](http://httpd.apache.org/docs/trunk/mod/mod_proxy_balancer.html) using the data from the heartbeats.


mod_heartbeat, mod_heartmonitor, and mod_ratelimit were all originally written at [Joost](http://www.joost.com/), and my employer was nice enough to let us contribute them back to Apache.

I've also announced the [intent to roll the first 2.3.0-alpha release next weekend](http://mail-archives.apache.org/mod_mbox/httpd-dev/200811.mbox/%3C49302488.5000002@force-elite.com%3E).  Hopefully this means within a few months, a new stable 2.4.x branch will come out.
