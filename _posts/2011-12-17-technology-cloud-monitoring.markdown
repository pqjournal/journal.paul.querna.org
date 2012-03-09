---
date: '2011-12-17 18:28:03'
layout: post
slug: technology-cloud-monitoring
status: publish
title: Technology behind Rackspace Cloud Monitoring
wordpress_id: '939'
---

Earlier this week we [announced a new product: Rackspace Cloud Monitoring](http://www.rackspace.com/cloud/blog/2011/12/15/announcing-rackspace-cloud-monitoring-private-beta/).  It is just starting as a (free) private beta, so if you want to try it out, be sure to [sign up via the survey here](https://surveys.rackspace.com/Survey.aspx?s=e08d057768e04f09a8cb7811d47b82da).





## Transition from Cloudkick Technology





Rackspace Cloud Monitoring is based on technology built originally for the [Cloudkick product](https://www.cloudkick.com/features/monitoring).   Some core concepts and parts of the architecture originated from Cloudkick, but many changes were made to enable Rackspace's scalability needs, improve operational support, and focus the Cloud Monitoring product as an API driven Monitoring as a Service, rather than all of Cloudkick's Management and Cloud Server specific features.





For this purpose, Cloudkick's product was successful in vetting many parts of the basic architecture, and serving as a basis on which to make a reasonable second generation system. We tried to make specific changes in technology and architecture that would get us to our goals, but without falling into an overengineering trap.





Cloudkick was primarily written in Python.  Most backend services were written in [Twisted Python](http://www.twistedmatrix.com/).  The API endpoints and web server were written in [Django](https://www.djangoproject.com/), and used [mod_wsgi](http://code.google.com/p/modwsgi/). We felt that while we greatly value the asynchronous abilities of Twisted Python, and they matched many of our needs well, we were unhappy with our ability to maintain Twisted Python based services.  Specifically, the deferred programming model is difficult for developers to quickly grasp and debug.  It tended to be 'fail' deadly, in that if a developer didn't fully understand Twisted Python, they would make many innocent mistakes.  Django was mostly successful for our needs as an API endpoint, however we were unhappy with our use of the Django ORM.  It created many dependencies between components that were difficult to unwind later.  Cloud Monitoring is primarily written in [Node.js](http://www.nodejs.org/). Our team still loves Python, and much of our secondary tooling in Cloud Monitoring uses Python. `[`EDIT: See standalone post: [The Switch: Python to Node.js](http://journal.paul.querna.org/articles/2011/12/18/the-switch-python-to-node-js/)`]`





Cloudkick was reliant upon a [MySQL](http://www.mysql.com/) master and slaves for most of its configuration storage. This severely limited both scalability, performance and multi-region durability.  These issues aren't necessarily a property of MySQL, but Cloudkick's use of the Django ORM made it very difficult to use MySQL radically differently.  The use of MySQL was not continued in Cloud Monitoring, where metadata is stored in Apache Cassandra.





Cloudkick used [Apache Cassandra](http://cassandra.apache.org/) primarily for metrics storage.  This was a key element in keeping up with metrics processing, and providing a high quality user experience, with fast loading graphs.  Cassandra's role was expanded in Cloud Monitoring to include both configuration data and metrics storage.





Cloudkick used the [ESPER engine](http://esper.codehaus.org/) and a small set of EPL queries for its Complex Event Processing.  These were used to trigger alerts on a monitoring state change.  ESPER's use and scope was expanded in Cloud Monitoring.





Cloudkick used the [Reconnoiter](http://labs.omniti.com/labs/reconnoiter) `noitd` program for its poller.  We have contributed patches to the open source project as needed.  Cloudkick borrowed some other parts of Reconnoiter early on, but over time replaced most of the Event Processing and data storage systems with customized solutions.  Reconnoiter's `noitd` poller is used by Cloud Monitoring.





Cloudkick used [RabbitMQ](http://www.rabbitmq.com/) extensively for inter-service communication and for parts of our Event Processing system.  We have had mixed experiences with RabbitMQ.  RabbitMQ has improved greatly in the last few years, but when it breaks we are at a severe debugging disadvantage, since it is written in Erlang.  RabbitMQ itself also does not provide many primitives we felt we needed when going to a fully multi-region system, and we felt we would need to invest significantly in building systems and new services on top of RabbitMQ to fill this gap. RabbitMQ is not used by Cloud Monitoring. Its use cases are being filled by a combination of [Apache Zookeeper](http://zookeeper.apache.org/), point to point REST or Thrift APIs, state storage in Cassandra and changes in architecture.





Cloudkick used an internal fork of [Facebook's Scribe](https://github.com/facebook/scribe) for transporting certain types of high volume messages and data.  Scribe's simple configuration model and API made it easy to extend for our bulk messaging needs.  Cloudkick extended Scribe to include a write ahead journal and other features to improve durability.  Cloud Monitoring continues to use Scribe for some of our event processing flows.





Cloudkick used [Apache Thrift](http://thrift.apache.org/) for some RPC and cross-process serialization.  Later in Cloudkick, we started using more JSON.  Cloud Monitoring continues to use Thrift when we need strong contracts between services, or are crossing a programing language boundary.  We use JSON however for many data types that are only used within Node.js based systems.






## Node.js ecosystem





We have been very happy with our choice of using Node.js.  When we started this project, I considered it one of our biggest risks to being successful -- what if 6 months in we are just mired in a new language and platform, and regretting sticking with the known evil of Twisted Python.  The exact opposite happened.  Node.js has been an awesome platform to build our product on.  This is in no small part to the many modules the community has produced.





Here it is, the following is the list of NPM modules we have used in Cloud Monitoring, straight from our package.json:

* [async](http://search.npmjs.org/#/async) (rackers patched it)
* [cassandra-client](http://search.npmjs.org/#/cassandra-client) (rackers wrote it)
* [cloudfiles](http://search.npmjs.org/#/cloudfiles)
* [command-parser](http://search.npmjs.org/#/command-parser) (rackers wrote it)
* [elementtree](http://search.npmjs.org/#/elementtree) (rackers wrote it)
* [express](http://search.npmjs.org/#/express)
* [ipv6](http://search.npmjs.org/#/ipv6) (rackers patched it)
* [jade](http://search.npmjs.org/#/jade)
* [logmagic](http://search.npmjs.org/#/logmagic) (rackers wrote it)
* [long-stack-traces](http://search.npmjs.org/#/long-stack-traces)  (rackers patched it)
* [magic-templates](http://search.npmjs.org/#/magic-templates) (rackers wrote it)
* [metrics](http://search.npmjs.org/#/metrics)
* [node-dev](http://search.npmjs.org/#/node-dev)
* [node-int64](http://search.npmjs.org/#/node-int64)
* [node-uuid](http://search.npmjs.org/#/node-uuid)
* [nodelint](http://search.npmjs.org/#/nodelint)
* [optimist](http://search.npmjs.org/#/optimist)
* [sax](http://search.npmjs.org/#/sax)
* [showdown](http://search.npmjs.org/#/showdown)
* [simplesets](http://search.npmjs.org/#/simplesets)
* [strtok](http://search.npmjs.org/#/strtok)
* [swiz](http://search.npmjs.org/#/swiz) (rackers wrote it)
* [terminal](http://search.npmjs.org/#/terminal) (rackers wrote it)
* [thrift](http://search.npmjs.org/#/thrift) (rackers patched it)
* [whiskey](http://search.npmjs.org/#/whiskey) (rackers wrote it)
* [zookeeper](http://search.npmjs.org/#/zookeeper) (rackers patched it)


Now that our product is announced, I'm hoping to find a little more time for writing. I will try to do more posts about how we are using Node.js, and the internals of Rackspace Cloud Monitoring's architecture.


_PS: as always, [we are hiring](http://rackertalent.com/san-francisco/) at our sweet new office in San Francisco, if you are interested, [drop me a line](mailto:paul.querna@rackspace.com)._



