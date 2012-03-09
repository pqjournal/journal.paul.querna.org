---
date: '2010-10-23 10:01:15'
layout: post
slug: three-things
status: publish
title: three things
wordpress_id: '451'
---

### Three things I would like to hear more about:





  
  * **DIRT**: [Data Intensive Real Time, coined by Bryan](http://dtrace.org/blogs/bmc/2010/10/02/the-dirt-on-jsconf-eu-and-surge/).  I've been thinking about how we use [orbited](http://orbited.org/) to do this, and I think a real revolution in web application infrastructure is just around the corner as more people get involved with Node.js type projects.


  
  * **Django non-rel**: An odd choice I think, but its these kind of projects that are taking a hard look at the ORMs most programmers have come to expect, and how to make their nice features feasible with very creative backends.  [Django non-rel](http://www.allbuttonspressed.com/projects/django-nonrel) won't be the last ORM on top of a non-relational datastore, and I think it will be years before its all settled out, but I know most people will never want to use [Cassandra's raw Thrift API](http://wiki.apache.org/cassandra/API).


  
  * **Upcoming Web Frameworks**: Hinted at by my first two, I think current web frameworks don't fit the evolving model of a web application.  Something that really combines a non-relational backend, with a process and communication model that supports DIRT, in addition to traditional HTML.  I don't think there is a leader here yet, but I think within a year or two, there will be serious disruption in the framework space -- a Rails or Django of the 2010s.  The key will be finding the right places of abstraction, because you still need to make it easy to use, even with all the crazy complicated things going on underneath, but if the wrong abstractions are selected, [you'll just end up with leaks everywhere](http://en.wikipedia.org/wiki/Leaky_abstraction).






### Three things I am tired of hearing about:





	
  * **Benchmarks of HTTP servers**: If the HTTP server is your applications bottleneck,  Congratulations!  But it probably means you are serving static files, and not using a database or a dynamic language.  HTTP is hard, but [Ryan has made it easier](http://github.com/ry/http-parser).  HTTP though, isn't the bottleneck on your Rails/PHP/Django/node.js application, some backend datastore will be.


	
  * **NoSQL**: I'm tired of some non-durable non-multi-master NoSQL projects.  We had that before, its called BDB in the 90s. Oh, and again with MySQL.  There are innovative NoSQL projects, stop polluting the name. Anyways, the name in general is terrible, but innovation is not building a new BDB, it is building a multi-master multi-datacenter data storage system.


  
  * **Meg Whitman vs Jerry Brown**: Only makes sense if you are a California resident I guess, but I don't like either candidate at this point.  Voting by mail, and just wish the election would be done, so I can stop seeing [their terrible attack advertisements](http://www.neontommy.com/news/2010/10/puppet-or-parrot-which-one-are-you-voting-governor-california) on each other.



