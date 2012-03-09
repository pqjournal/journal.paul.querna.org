---
date: '2007-07-14 15:53:00'
layout: post
slug: announcement-cluster-tail-released
status: publish
title: 'announcement: cluster tail released'
wordpress_id: '197'
---

I'm happy to announce the release of a new piece of software that I've written. [Cluster Tail](http://ctail.i-want-a-pony.com/) or `ctail` for short.  Basically, it multiplexes lots of SSH connections, to invoke `tail -f` on a large set of machines or log files.





It isn't the most amazing idea, but if you have ever had hundreds of machines (or even a dozen), trying to understand what is going on across all of can be very difficult, and this is just another tool to make that easier.





Most other methods of reading log files on large clusters get away from [classic Unix Philosophy](http://en.wikipedia.org/wiki/Unix_philosophy), but `ctail` can easily be piped into other commands.
