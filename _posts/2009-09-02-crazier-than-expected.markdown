---
date: '2009-09-02 08:09:25'
layout: post
slug: crazier-than-expected
status: publish
title: crazier than expected.
wordpress_id: '317'
---

Last week ended with a boom.  I was about to [start upgrading wiki.apache.org](http://twitter.com/infrabot/status/3598230658) to a modern version of MoinMoin when I noticed some odd CGIs running on www.apache.org.  All of that mess is just about over now.  We (royal) have put up an [initial report](https://blogs.apache.org/infra/entry/apache_org_downtime_initial_report), and just today put up a [report with more details](https://blogs.apache.org/infra/entry/apache_org_downtime_report) and some of the actions we are taking in response.

The coolest thing coming out of it is some motivation to finish [SvnPubSub](https://svn.apache.org/repos/infra/infrastructure/trunk/projects/svnpubsub/svnpubsub.py).  You can try it out right now, it is running on our svn-master:


> curl -i http://svn-master.apache.org:2069/dirs-changed/xml


(data formats, URLs, etc will change, don't use it for anything special yet)

The whole apache.org incident though has killed my time for hacking on serf, but I'll hopefully find some time to finish the server support soon.

Other misc stuff:



	
  * Moving up to San Francisco in the next month, will do another post with more details later.

	
  * Cloudkick is going well, doing fun stuff with Python and Twisted, hopefully have more to blog about there soon.


