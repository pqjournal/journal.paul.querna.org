---
date: '2010-11-02 07:44:45'
layout: post
slug: the-case-for-gossip
status: publish
title: The case for Gossip
wordpress_id: '743'
---

More of a stream than a full blog post.

Lets say your business is a website, and this means downtime is unacceptable.

Lets also you don't have ops people in 3 spread out timezones. (Hey, you aren't Google)

This means at some point, your ops people go to sleep.

Ops people hate getting woken up at night.

Gossip can reduce the times ops teams are woken up. ([If it doesn't cause your website to be down for hours](http://www.facebook.com/notes/facebook-engineering/more-details-on-todays-outage/431441338919))

Gossip doesn't mean you automatically determine the **role** of a machine.

Gossip is not autoscalling. Not Autogrowing. Not Auto-lots of things.

Gossip is **discovering** the current state of your machines.

It does mean you have a faster convergence time on failure, which reduces the cost of a failure, and reduces the pain inflicted on your ops people.

I believe you still want a human involved in many auto things.  Use humans to add new machines, to change their roles, to do capacity planning.

Automatically **determining where** resources are within your network, not allocating them.  Allocating and destroying automatically is a different topic, and should be addressed, differently.

Finding available resources is different than just configuration management.  Availability is not a concept something like puppet or chef have.

They have variables, ways to acquire them, and high latency ways to propagate them.

The time to failure detection in a properly written gossip system can be sub-second, depending on your application's needs.

That is order of magnitudes faster than a human, or a configuration management system, or a human changing a configuration management environment.

There are some alternatives you could use instead of gossip.  They include things like load balancers, which can have their own host of issues.

You can use things like Zookeeper, but underneath they are just gossiping underneath.

You can use things like DNS, but now you are using DNS (insert dns rant here).

You can write your application to be more robust, and re-try different machines on failure, but then you generally are adding latency to an end user request.  Making your application more robust, I believe is relevant, but a divergent topic. You'll still want to wake up an ops person though, because adding latency to even a subset of requests is not acceptable.

Gossip isn't perfect.  Gossip doesn't solve everything.  Gossip, like most things, can be abused and overused.  I believe Gossip however, used for a limited goal of reducing the time to detection and the impact of failures, is overall a positive mechanism for most infrastructures.


