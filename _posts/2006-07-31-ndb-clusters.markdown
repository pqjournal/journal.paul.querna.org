---
date: '2006-07-31 21:56:00'
layout: post
slug: ndb-clusters
status: publish
title: ndb clusters
wordpress_id: '159'
---

So, [MySQL AB](http://www.mysql.com/) has a huge chunk of [new documentation on the NDB API](http://dev.mysql.com/doc/ndbapi/en/index.html).




Short Story: [Semi-sleepycat](http://www.sleepycat.com/docs/gsg/C/index.html) like API available, but its replicated/clustered and everything magically. [Example](http://dev.mysql.com/doc/ndbapi/en/example-synchronous-transactions.html)






[Brian Aker](http://krow.net/) was at the memcached [BOF](http://en.wikipedia.org/wiki/BOF) at OSCON, saying how it is way cool, and could be used in some places to replace [memcached](http://www.danga.com/memcached/).





But, what I haven't found is anyone talking about using the ndbclient API in large scary production environments. **Is there anyone out there really hammering it?**





Infact, a [Google Search for "ndbclient"](http://www.google.com/search?q=ndbclient&ie=utf-8&oe=utf-8) only returns 111 results right now, none of which look too great.





It seems like it could be a great solution instead of using application level partitioning and [replicating Berkeley DB](http://www.sleepycat.com/docs/ref/rep/intro.html) in some use cases. I don't mind being given a low level API and having to build my application level logic on top... It's how Sleepycat has worked for 20 years.



