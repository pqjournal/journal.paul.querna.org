---
date: '2005-09-05 11:31:37'
layout: post
slug: async-io-in-httpd-2-3
status: publish
title: Async IO in HTTPD 2.3
wordpress_id: '97'
---


In the last couple days ideas and code for doing asynchronous writes to clients has started to flow.  Brian Pane has [posted a cool diagram ](http://www.brianp.net/work/opensource/apache/async.html)of how the different connection states might work. On Saturday I created a subversion branch at [https://svn.apache.org/repos/asf/httpd/httpd/branches/async-dev/](https://svn.apache.org/repos/asf/httpd/httpd/branches/async-dev/) to house the development.  If anyone is interested in helping shape Async IO development, please go and criticize our plans on [dev@httpd](http://httpd.apache.org/lists.html#http-dev).



I hope to have time to post a more detailed description of the work and ideas on this blog.... Maybe later this week.

