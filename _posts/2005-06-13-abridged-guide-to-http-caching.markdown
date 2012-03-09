---
date: '2005-06-13 02:46:00'
layout: post
slug: abridged-guide-to-http-caching
status: publish
title: Abridged guide to HTTP Caching
wordpress_id: '76'
---

At the highest level, HTTP is a very simple protocol.  It is quite easy to write both a server and a client.  However, the parts of the standard that control Cacahing of HTTP Requests become complex very quickly.  So complex, that most web applications do not behave correctly. So here is "`chip's abridged guide to HTTP Caching for Web Application Developers`".





**The Vary Header**  

Simple Rule: If you look at **any** header from the client, and do something based on it, you **must** add it to the Vary header.  This means if you use the User-Agent, the Accept-Encoding, or any Cookies, you must add them to the Vary Header.  
  

The [ASF Wiki](http://wiki.apache.org/general/) uses [MoinMoin](http://moinmoin.wikiwikiweb.de/).  I would venture to say that it is one of the most popular Wiki software available.  Despite popularity, it doesn't handle the Vary Header correctly at all.  Due to excessive load on the wiki server, [mod_cache](http://httpd.apache.org/docs-2.1/mod/mod_cache.html) was added. People browsing the site quickly had problems.  Users would get pages in different languages.  Sometimes you would get a page with different person's login.  This wasn't the fault of mod_cache, infact, the same problems would happen with any [downstream caching proxy](http://webmaster.info.aol.com/caching.html).
  

  

To start fixing MoinMoin, you need to add **`Vary: Cookie,Accept-Encoding`** to the output for every page.  This means for every different value of the Cookie headers and the Accept-Encoding, mod_cache will cache a different version.  If you do not do this, people will get the page in the wrong language, or with someone else's login.



  
  




**The Cache-Control Header**  

Simple Rule: You must use this for **any** personalized page. If you have any information that is specific to a logged in user, you **must** use the Cache-Control Header.  
  

Now, Cache-Control is harder to put into a simple box, because it can be used to control many different things.  For most applications however, it can be shortened to 'If you have private content, you must add **`Cache-Control: private, must-revalidate`**.
  
  
MoinMoin doesn't do this for pages generated for logged in users.  This means it is possible for another user to see a different user's logged in page, as it was cached.  This is mostly harmless and more annoying in the MoinMoin case, but for other applications, you might have private information that you do not want cached.


  
  




If you follow those two relatively simple rules, most web applications will at the very least behave correctly behind an HTTP Cache.  For details, there is always [the RFC](http://www.faqs.org/rfcs/rfc2068.html), but [some](http://webmaster.info.aol.com/faq.html#cachingfaq) [other](http://drupal.org/node/18390) [sites have more friendly](http://wp.wikidev.net/MediaWiki_caching) [information](http://www.web-caching.com/mnot_tutorial/).





**Update:** Added `must-revalidate` to the Cache-Control section.
