---
date: '2010-01-25 23:10:12'
layout: post
slug: cloudkick-agent-and-more
status: publish
title: Released Cloudkick's for-pay products
wordpress_id: '326'
---

I started at Cloudkick in August, and [today we announced our for-pay products & Freemium model](https://www.cloudkick.com/pricing).  ([TechCrunch](http://www.techcrunch.com/2010/01/25/cloudkick-rolls-out-freemium-model-for-server-management-system/), [GigaOm](http://gigaom.com/2010/01/25/cloudkick/), [ReadWriteWeb](http://www.readwriteweb.com/enterprise/2010/01/cloudkick---helping-customers.php), [VentureBeat](http://venturebeat.com/2010/01/25/cloudkick/), and [more](http://news.google.com/news/search?aq=f&pz=1&cf=all&ned=us&hl=en&q=cloudkick))

I've been working along with the entire Cloudkick Team on a few parts of our launch:



	
  * Integration with [Apache libcloud](http://incubator.apache.org/libcloud/), so now Cloudkick supports EC2, Rackspace, Slicehost, RimuHosting, Linode, VPS.net and GoGrid.

	
  * Our new monitoring Agent, [Cloudkick Agent.](https://support.cloudkick.com/Agent/Installation) Extremely light weight, written in C & Lua.  Hopefully I'l have some time to blog more about some of the cool technology we did here, but we were tired of seeing monitoring agents written in High Level languages using up tons of memory on a Cloud Server.

	
  * Our Cloudkick Changelog Tool, aka "ckl".  This tool lets you keep track of a large admin team and what everyone is doing.  The ASF Infrastructure team has already [started using it outside of Cloudkick](http://monitoring.apache.org/ckl.cgi).  Of course, the Cloudkick UI is a little nicer than [the demo one with the open source code](http://github.com/pquerna/ckl).

	
  * Our new [Graphing and long term trending system,](https://www.cloudkick.com/site_media/images/home_tour/graphs.png) built on top of [Reconnoiter](https://labs.omniti.com/trac/reconnoiter) and [Apache Cassandra](http://incubator.apache.org/cassandra/).

	
  * Learned more about Django and JQuery than ever before.


Now that our big launch is out, hopefully I'll find a little more time to post on this journal more.
