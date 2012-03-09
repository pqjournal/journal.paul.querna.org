---
date: '2005-12-02 12:25:23'
layout: post
slug: httpd-2-2-0-released
status: publish
title: HTTPD 2.2.0 Released
wordpress_id: '114'
---


I was the release manager for Apache HTTPD 2.2.0.  I have to say, being the release manager was the hardest thing I have ever done for Apache HTTPD.  I think now that the 2.2.x branch is started, it will hopefully be an easier task.  This also means we have are 2.3-dev on [/trunk/](https://svn.apache.org/repos/asf/httpd/httpd/trunk/).  I am hoping to find time to help with the [improved async work](https://svn.apache.org/repos/asf/httpd/httpd/branches/async-read-dev/) on the [Event MPM](http://httpd.apache.org/docs/trunk/mod/event.html).



After 9 alphas and beta in the last year, 2.2 is the next 'stable' branch of Apache.  Its a relatively easy jump from 2.0 too, but adds [lots of new features](http://httpd.apache.org/docs/2.2/new_features_2_2.html). You should upgrade now.



We finally sent the [release announcement](http://mail-archives.apache.org/mod_mbox/httpd-announce/200512.mbox/%3c438F7076.6090801@apache.org%3e) yesterday. Coverage from the RSS Feeds and searches:




  * [ZDNet](http://www.zdnet.com.au/news/software/soa/New_Apache_aims_to_please/0,2000061733,39225677,00.htm) (same article on [Builder.com](http://uk.builder.com/0,39026540,39286878,00.htm))- Kinda weird quoting the announcement like it was a press release. They also mention the [RFP for helping with the ASF's Infrastructure](http://www.apache.org/dev/rfp/).


  * [Slashdot](http://apache.slashdot.org/article.pl?sid=05/12/02/0124224&tid=162&tid=95&tid=164&tid=2) - Smattering of comments all over the board.  Seems like most people do like the Large File Support. At least [one person](http://apache.slashdot.org/comments.pl?sid=169930&cid=14165533) likes the new [httpd -M](http://httpd.apache.org/docs/2.2/programs/httpd.html#options) option, which dumps all loaded modules.  I think that feature will be one of the best for helping confused users.


  * [Brad](http://www.livejournal.com/users/brad/2180763.html) - says: "_Looks like most the stupid shit has been fixed:_" Which, is a pretty good way to describe the 2.2 feature set.   Lots of low hanging fruit fixes and features


  * [collmmacc](http://www.stdlib.net/~colmmacc/2005/12/01/apache-httpd-220-released/) - No comments, but I will try to help increase his page rank.


  * [JimJag](http://www.jimjag.com/imo/index.php?/archives/50-guid.html) - Notes that Apache 1.0.0 was released on the same day 10 years ago.  Even if most of the original developers are no longer active, the project is still successful.  I believe this is one of the most undervalued attributes of community, and hopefully other open source projects will learn that its the community that matters to long term success, not fighting over silly features.


  * [Gentoo Bugzilla](http://bugs.gentoo.org/show_bug.cgi?id=114232) - Already have an open bug, requesting the ebuild.




A **HUGE** round of thanks to the [many other](http://httpd.apache.org/contributors/) Apache HTTP Server developers.

