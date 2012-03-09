---
date: '2007-10-25 19:13:15'
layout: post
slug: new-software-mod_timer
status: publish
title: 'new software: mod_timer'
wordpress_id: '215'
---

Do you have a custom logging module?

Ever wondered how long it took to actually finish logging?

At $[work](http://www.ask.com) I was helping with some problems with Apache, and we wanted to know how long until an Apache Worker Process actually goes back into the Accept Queue.

So [mod_timer](http://people.apache.org/~pquerna/modules/mod_timer.c) is born. It hooks into Apache when the connection is accepted, before we start reading any data, and the timer ends when the connection memory pool is destroyed.  It also performs the same measurements on [requests inside the connection](http://www.w3.org/Protocols/rfc2616/rfc2616-sec8.html).

It produces a log file like this:


> r:127.0.0.1:51886:1193364411078414:1568
r:127.0.0.1:51886:1193364411077069:3034
r:127.0.0.1:51886:1193364411080117:21150
r:127.0.0.1:51886:1193364411101293:99477
r:127.0.0.1:51886:1193364411200792:1856762
r:127.0.0.1:51886:1193364413057577:7000364
c:127.0.0.1:51886:1193364411077016:8980955
r:127.0.0.1:51887:1193364427909070:96608
r:127.0.0.1:51887:1193364428006034:2031335
r:127.0.0.1:51887:1193364430037392:1086699
r:127.0.0.1:51887:1193364431124508:916482
r:127.0.0.1:51887:1193364432041014:5315190
c:127.0.0.1:51887:1193364427909020:9447211


Log Fields:



	
  * 'r' or 'c' represents if this is a request or connection being logged.

	
  * Remote IP Address

	
  * Remote Port

	
  * Start time, in [apr_time_t](http://apr.apache.org/docs/apr/trunk/group__apr__time.html) (64bit int time since 1970 in microseconds)

	
  * Run time in microseconds


Using this, it becomes easier to look for 'evil' clients that are doing things like sending one byte of a GET request a second.
