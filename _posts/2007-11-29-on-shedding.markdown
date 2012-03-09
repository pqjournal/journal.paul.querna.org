---
date: '2007-11-29 03:25:04'
layout: post
slug: on-shedding
status: publish
title: on shedding
wordpress_id: '219'
---

Brian McCallister has a [new post on a service location technique dubbed "Shredding"](http://kasparov.skife.org/blog/src/shedding.html).This post started out as a comment on Brian's site, but it got a little long....



	
  * Don't underestimate using load balancers where they make sense..  You don't need to spend tons of money on a commercial one.  2x 1u pizza boxes with modern CPUs + 1/10GigE running [{Free,Open}BSD + CARP + pfsync.](http://www.openbsd.org/faq/pf/carp.html)

	
  * For 'dumb clients': Just Proxy it.  Perlbal does this for LiveJournal infront of their [MogileFS](http://www.danga.com/mogilefs/) boxes.  Or look at Dynamo for another example, the 'dumb' clients can connects to any nodes, and that nodes proxies to the correct one.  Reducing the number of request/response cycles down is important to keep client latency down.  Its not so much about the persistent TCP connection, as the send/reply of the data just to find something.

	
  * For 'smart clients': I personally prefer a [daemon](http://mail-archives.apache.org/mod_mbox/labs-labs/200612.mbox/%3C4583132B.7090304@apache.org%3E) running on each local machine, which uses a multicast/gossip communication with other nodes to keep a local 'cache' of where services are located and their status. Every couple seconds, based on the current state of the cluster, it would write it out to blob file on disk.  Clients Just slurp up this file to find anything. (You can also do the same thing, but based on a unix daemon socket, but its generally slower.)

	
  * There is some discussion about RFC issues with 302s and sending a POST to the redirected URL.  The larger issue is that almost no HTTP Client Libraries will do this correctly out of the box.


All that said, for the Bloglines FS, we proxy writes to the data storage nodes, but that is mostly to ensure redundancy of data. For reads, we send back a sorted list of the data nodes that have a chunk to the client.  The client then connects directly, and will try the other entries on the list if the first one fails.

See also:

	
  * [dislocate - my unfinished apache labs project](http://mail-archives.apache.org/mod_mbox/labs-labs/200612.mbox/%3C4583132B.7090304@apache.org%3E).

	
  * [Python urlib2 issue #1401: 302 handling](http://bugs.python.org/issue1401)

	
  * HTTPClient issues: [HTTPCLIENT-245](https://issues.apache.org/jira/browse/HTTPCLIENT-245) [HTTPCLIENT-128](https://issues.apache.org/jira/browse/HTTPCLIENT-128)

	
  * [slbd - OpenBSD server load balancing using PF](http://slbd.sourceforge.net/).


