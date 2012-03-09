---
date: '2008-04-08 23:19:53'
layout: post
slug: apache-http-server-development-for-this-week
status: publish
title: Apache HTTP Server development for this week
wordpress_id: '229'
---





The last week has seen many new features and improvments made to httpd.  Many of them have been [accelerated](http://www.ohloh.net/projects/apache) by people at the [ApacheCon EU Hackathon](http://www.flickr.com/search/?q=apachecon&s=rec) this week. 







  * **mod_session**

On Friday [Graham Leggett](http://www.ohloh.net/projects/apache/contributors/311385142451) introduced a series of modules to support generation of sessions from HTTPD.  Included is mod_session_crytpo, which encrypts the data using AES.  This is the first time 'form based' authentication has had real support in the Apache Core.   
[docs: mod_session](http://httpd.apache.org/docs/trunk/mod/mod_session.html) 
[thread: Apache support for form authentication](http://mail-archives.apache.org/mod_mbox/httpd-dev/200804.mbox/%3c47F6432A.9060402@sharp.fm%3e)







  * **mod_socache**

On Tuesday [Joe Orton](http://www.ohloh.net/projects/apache/contributors/309237654848) committed the new Small Object Cache modules, which have been under discussions for a couple months now.  The `mod_ssl` session cache has been changed to use this.  Currently supported cache backends are DBM, memcached, and Shared Memory.  I expect many other modules will changed to use this cache API as time goes on.  
[svn: `ap_socache.h`](http://svn.apache.org/repos/asf/httpd/httpd/trunk/modules/cache/ap_socache.h) 
[thread: PATCH `ap_socache.h` `mod_socache`](http://mail-archives.apache.org/mod_mbox/httpd-dev/200804.mbox/%3c20080408105325.GA2464@redhat.com%3e)  








  * **If/Else blocks added**

[Nick Kew](http://www.ohloh.net/projects/apache/contributors/311385142454) ported the expression parser from mod_includes, and has used this to add If and Else blocks to the core.This provides a viable alternative to mod_rewrite and RewriteCond, and letsyou set any modules configuration values.   
[docs: if](http://httpd.apache.org/docs/trunk/mod/core.html#if) 
[thread: Dynamic configuration for the hackathon?](http://mail-archives.apache.org/mod_mbox/httpd-dev/200803.mbox/%3C20080326130647.7f9ae161@grimnir%3E) 
[commit: r644253](http://svn.apache.org/viewvc?view=rev&revision=644253)







  * **Turkish Documentation**

Nilgün Belma Bugüner contributed a complete translation of the Apache HTTP Server documentation in Turkish.   
[docs: Turkish](http://httpd.apache.org/docs/trunk/tr/) 
[thread: New Turkish Documents](http://mail-archives.apache.org/mod_mbox/httpd-docs/200804.mbox/%3C200804071045.47224@belgeler.gen.tr.ileti.no%3E) 
[commit: r645667](http://svn.apache.org/viewvc?view=rev&revision=645667)








  * **Serf Bucket Discussions**

Discussion at the Hackathon covered how [Serf Buckets](http://code.google.com/p/serf/source/browse/trunk/design-guide.txt) use a "pull" method, for both input and output, unlike the current filter stack in httpd, which is Pull for input filters, but push for output filters. There was general agreement that the expieriment  of mod_serf should be expanded up the filter stack.   
[svn: mod_serf.c](http://svn.apache.org/repos/asf/httpd/sandbox/amsterdam/d/modules/proxy/mod_serf.c)








  * **Simple MPM created**

[Paul Querna](http://www.ohloh.net/projects/apache/contributors/311385142467) started work on a new MPM at the Hackathon. The MPM hopes to run on both Unix and Win32 platforms, and keep the same behavoirs on both.   
[svn: SIMPLE.README](http://svn.apache.org/repos/asf/httpd/sandbox/amsterdam/d/server/mpm/simple/SIMPLE.README)









