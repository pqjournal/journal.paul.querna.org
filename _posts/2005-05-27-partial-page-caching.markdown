---
date: '2005-05-27 11:32:26'
layout: post
slug: partial-page-caching
status: publish
title: Partial Page Caching?
wordpress_id: '74'
---

Over-generalizing, there are 3 common places to add caching in a web based application:


  * Data Level Caching

  * Full Page Caching

  * Partial Page Caching


  

Data Level Caching means when you do a complex SQL Query or fetching some remote data, you keep a copy of it locally, or in something like [memcached](http://www.danga.com/memcached/).  
  

Full Page Caching can be done both inside the application via something like [Smarty](http://smarty.php.net/manual/en/caching.php), or at the HTTP level with [mod_cache](http://httpd.apache.org/docs-2.1/mod/mod_cache.html) or [Squid](http://www.squid-cache.org/).
  
  

What perplexes me is the lack of open source tools that help with Partial Page Caching.  The best 'open' standard for it is [Edge Side Includes](http://www.esi.org/).  But, just look at the ESI site, the last 'news' item was from 2002.  It looks quite dead, and I cannot find any recent chatter about it anywhere.  Do people just not do Partial Page Caching?  Is it even worth it?
  
  

In my experience, doing data level caching can make the biggest difference, to avoid hitting databases or very slow backends, but I am surprised at the lack of open source software using partial page caching. For both of the other caching methods, there are very very good open source tools to help you do the _work_ of caching, but for a Partial Page Cache, I haven't seen any tools to help you.  Maybe there just isn't a very big need, since once you have the data cached, going to the _next level of performance_ many times means caching the entire page...
