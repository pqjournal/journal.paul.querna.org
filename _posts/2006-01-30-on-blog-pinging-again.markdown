---
date: '2006-01-30 10:55:35'
layout: post
slug: on-blog-pinging-again
status: publish
title: On Blog Pinging (again)
wordpress_id: '122'
---


Dear Internet,



When a [major ping service has problems](http://newestindustry.wordpress.com/2006/01/29/ping-o-matic-meet-ping-o-death/), I will remind you that [Blog Pings are stupid](http://paul.querna.org/journal/articles/2005/09/28/blog-pings-are-stupid). Some companies [rely upon blog pings for their crawling system](http://www.technorati.com/weblog/2006/01/75.html).   What happens when a ping service is down? Your posts don't get indexed.  Oh Snap.



[People have noticed](http://blogfresh.blogspot.com/2006/01/pinging-for-mutual-benefit.html) that if you want to get higher rankings in some search engines, you should find everyone who has linked to you, and [send Pings for them](http://www.technologyevangelist.com/2006/01/technorati_link_opti.html).   Ping-spoofing. It really feels like email-spoofing to me.  Maybe SPF could be extended to prevent this......



Anyways, At [$work](http://www.bloglines.com/) we do not currently accept pings from anyone.  Instead we crawl every site in our system, every 30 minutes.  Its not that hard, honestly, thanks to [memcached](http://www.danga.com/memcached/) and [conditional http requests](http://fishbowl.pastiche.org/2002/10/21/http_conditional_get_for_rss_hackers). (Oh, and lots of bandwidth).



Blog Pings have fundamental problems.  Until they are both **reliable** and **secure**, I hope they will die. (By secure I mean knowing that the person who sent the ping is the person who owns the feed....).  [FeedTree](http://www.feedtree.net/) tries to go down this path.  It has many problems, the foremost is using Java.  If you want everyone in the world to support your protocol, you need support for everyone still using c, perl, python, php, and ruby.  The other problem with FeedTree, is that it makes crypto signing of pings optional.  Rule number one of making a spec: Nothing is optional, because anything that is, won't be implemented by half the software out there.



Have a happy Monday.



-Paul

