---
date: '2005-04-16 19:54:55'
layout: post
slug: browser-detection-is-bad
status: publish
title: Browser Detection.. is bad.
wordpress_id: '69'
---

[UMO](http://update.mozilla.org) uses browser detection to try to determine which version of some extensions you want to download.  For example, the Enigmail Extension, you need a version for every OS, including Windows, Linux and OS X. Look at the [Enigmail Page](https://addons.update.mozilla.org/extensions/moreinfo.php?application=thunderbird&category=Privacy%20and%20Security&numpg=10&id=71).
  
  

Well, I see a download for Windows, but I am using OS X.  When you visit it, you might see it for Linux, or OS X -- its hard to tell, since the page is cached with a [Squid frontend](http://www.squid-cache.org/), you get the download link for whatever OS viewed the page before you.  
  

The solution is to add a `Vary: User-Agent` HTTTP header, to make the cache use a different version of the Cache for every User Agent -- and therefore show the correct download link.  The bad news is that Squid doesn't support the Vary header.  I geuss the only option is [Apache 2.1](http://httpd.apache.org/docs-2.1/mod/mod_cache.html).
