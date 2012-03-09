---
date: '2011-12-18 01:33:06'
layout: post
slug: the-switch-python-to-node-js
status: publish
title: 'The Switch: Python to Node.js'
wordpress_id: '955'
---

In [my previous post](http://journal.paul.querna.org/articles/2011/12/17/technology-cloud-monitoring/), I glossed over our team switching from Python to Node.js.  I kept it brief because the switch wasn't the focus of the post, but since I believe I am being misunderstood, I will explain it in depth:




> Cloudkick was primarily written in Python.  Most backend services were written in [Twisted Python](http://www.twistedmatrix.com/).  The API endpoints and web server were written in [Django](https://www.djangoproject.com/), and used [mod_wsgi](http://code.google.com/p/modwsgi/). We felt that while we greatly value the asynchronous abilities of Twisted Python, and they matched many of our needs well, we were unhappy with our ability to maintain Twisted Python based services.  Specifically, the deferred programming model is difficult for developers to quickly grasp and debug.  It tended to be 'fail' deadly, in that if a developer didn't fully understand Twisted Python, they would make many innocent mistakes.  Django was mostly successful for our needs as an API endpoint, however we were unhappy with our use of the Django ORM.  It created many dependencies between components that were difficult to unwind later.  Cloud Monitoring is primarily written in [Node.js](http://www.nodejs.org/). Our team still loves Python, and much of our secondary tooling in Cloud Monitoring uses Python.


This attracted a few tweets, [accusing various things about our developers,](https://twitter.com/#!/g0rm/status/148284022181732354) but I want to explore the topic in depth, and 140 characters just isn't going to cut it.




## Just how much Python did Cloudkick have?



We had about 140,000 lines of Python in Cloudkick.  We had 40 [Twisted Plugins](http://twistedmatrix.com/documents/current/core/howto/plugin.html).  Each Plugin roughly corresponds to a backend service. About 10 of them are random DevOps tools like IRC bots and the like, leaving about 30 backend services that dealt with things in production.  We built most of this code in a 2.5 year experience, growing the team from the 3 founders to about a dozen different developers.  I know there are larger Twisted Python code bases out there, but I do believe we had a large corpus of experiences to build our beliefs upon.

This wasn't just a weekend hack project and a blog post about how I don't like deferreds, this was 2.5 years of building real systems.



## It worked.



[We were acquired.](http://www.rackspace.com/information/newsroom/pressreleases/rackspace-acquires-cloudkick-to-provide-powerful-server-management-tools-for-the-cloud-computing-era/)

Our Python code got the job done.  We built a product amazingly quickly, built our users up, and were able to iterate quickly.  I meant it when I said our team still **still loves Python**. 

What I didn't mention in the original post, is that after the acquisition, the Cloudkick team was split into two major projects -- Cloud Monitoring, which the previous post was about, and another unannounced product team.  This other product is being built in Django and Twisted Python.  Cloud Monitoring has very different requirements moving forward -- our goals are to survive and keep working after [a truck drives into our data centers](http://www.datacenterknowledge.com/archives/2007/11/13/truck-crash-knocks-rackspace-offline/), and this is very different from how the original Cloudkick product was built.




## What happened to Python then?



Simply put, our requirements changed.  These new requirements for Cloud Monitoring included:





  * Multi-Region availability / durability


  * Multiple order of magnitude increases in servers monitored


  * Scalable system, that can still be used 5 year from now. (Remember Rackspace Cloud [grew 89% year over year right now](http://seekingalpha.com/article/306015-rackspace-hosting-s-ceo-discusses-q3-2011-results-earnings-call-transcript))



Cloudkick was built as a startup.  We took shortcuts.  It scaled pretty damn well, but even if we changed nothing in our technology stack, it was clear we needed to refresh our architecture and how we modeled data.

The mixing of both blocking-world Django, and Twisted Python also created complications.  We would have utility code that could be called from both environments. This meant extensive use of `deferToThread` in order to not block Twisted's reactor thread.  This created an overhead for every programmer to understand both how Twisted worked, and how Django worked, even if your project in theory only involved the web application layer.  Later on, we did build enough tooling with function decorators to reduce the impact of these multiple environments, but the damage was done.

I believe our single biggest mistake from a technical side was not reigning in our use Django ORM earlier in our applications life.  We had Twisted services running huge Django ORM operations inside of the Twisted thread pool.  It was very easy to get going, but as our services grew, not only was this not very performant, and it was extremely hard to debug.  We had a series of memory leaks, places where we would reference a QuerySet, and hold on to it forever.  The Django ORM also tended to have us accumulate large amounts of business logic on the model objects, which made building strong service contracts even harder.

These were our problems.  We dug our own grave.  We should've used [SQLAlchemy](http://www.sqlalchemy.org/).  We should've built stronger service separations.  But we didn't.  Blame us, blame Twisted, blame Django, blame whatever you like, but thats where we were.

We knew by April 2011 that the combination of new requirements and a legacy code base meant we needed to make some changes, but we also didn't want to fall into a "Version 2.0" syndrome and over engineering every component.



## Picking the Platform.



We wanted some _science_ behind this kind of decision, but unfortunately this decision is about programming languages, and everyone had their own opinions.  

We wanted to avoid "just playing with new things", because at the time half our team was enamored with [Go Lang](http://golang.org/).  We were also very interested in [Python Gevent](http://www.gevent.org/), since OpenStack Nova had recently switched to it from Twisted Python.

We decided to make a [spreadsheet of the possible environments](https://docs.google.com/spreadsheet/ccc?key=0AvBGESHWxhk2dHJ2Q0lWRFF3dkxLZmFiMVVGRElQaEE) we would consider using for our next generation product.  The inputs were:

* Community
* Velocity
* Correctness (aka, static typing-like things)
* Debuggability/Tooling
* Downtime/Compile Time
* Libraries (Standard/External)
* Testability
* Team Experience
* Performance
* Production



We setup the spreadsheet so we could change the weight of each category.  This let us play with our feelings, what if we only cared about developer velocity? What if we only cared about testability?

Our conclusion was, that it came down to was a choice between the JVM platform and Node.js.  It is obvious that the JVM platform is one of the best ways to build large distributed systems right now.  Look at everything [Twitter](https://github.com/twitter), [LinkedIn](http://engineering.linkedin.com/tags/sna) and others are doing.  I [personally have serious reservations](http://journal.paul.querna.org/articles/2010/10/12/java-trap-2010-edition/) about investing on top of the JVM, and Oracles recent behavior ([here](https://news.ycombinator.com/item?id=3294783), [here](https://news.ycombinator.com/item?id=3357623)) isn't encouraging.


After much humming and hawing, we picked Node.js.

After picking Node.js, other choices like using Apache Cassandra for all data storage were side effects -- there was nothing like SQL Alchemy for Node.js at the time, so we were on our own either way, and Cassandra gave us definite improvements in operational overhead of compared to running a large number of MySQL servers in a master/slave configuration.



## Node.js? It has nested callbacks everywhere, thats ugly!



I think this is one of the first complaints people lob at Node.js when they just start.  It makes a regular occurrence on the users mailing list -- people think they want coroutines, generators or fibers.

I believe they are wrong.

**The zen of Node.js is its minimalist core**, both in size and in features.  You can read the core lib Javascript in a day, and one more day for the C++.  Don't venture into v8 itself, that is a rabbit hole, but you can pretty quickly understand how Node.js itself works.

Our experience was that we just needed to pick one good tool to contain callback flows, and use it everywhere.

We use [@Caolan's](https://twitter.com/Caolan) excellent [Async library](https://github.com/caolan/async).  Our code is not 5 level deep nested callbacks.  

We currently have about 45,000 lines of Javascript in our main repository.  In this code base, we have used the `async` library as our only flow control library.  Our current use of the library in our code base:

* `async.waterfall`: 74
* `async.forEach`: 55
* `async.forEachSeries`: 21
* `async.series`: 8
* `async.parallel`: 4
* `async.queue`: 3


I highly suggest, that if you are unsure about Node.js and are going to do an experiment project, make sure you use [Async](https://github.com/caolan/async), [Step](https://github.com/creationix/step), or one of the other flow control modules for your experiment.  It will help you better understand how most larger Node.js applications are built.



## Closing



In the end, we had new requirements.  We re-evaluated what platforms made sense for us to build a next generation product on.  Node.js came out on top.  We all have our biases, and our preferences, but I do believe we made a reasonable choice.  Our goal in the end is still to move our product forward, and improve our business.  Everything else is just a distraction, so pick your platform, and get real work done.


PS: If you haven't already read it, read SubStack's great [the node.js aesthetic](http://substack.net/posts/b96642/the-node-js-aesthetic) post.
