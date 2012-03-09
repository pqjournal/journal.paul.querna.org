---
date: '2005-07-02 12:17:00'
layout: post
slug: blog-software-http-caching
status: publish
title: Blog Software and HTTP Caching
wordpress_id: '84'
---

I took a look at 7 different weblog engines this afternoon:




  * [Blog::CMS](http://blogcms.com/)


  * [bBlog](http://www.bblog.com/)


  * [b2evolution](http://b2evolution.net/)


  * [Serendipity](http://www.s9y.org/)


  * [TextPattern](http://textpattern.com/)


  * [Typo](http://typo.leetsoft.com/trac/)


  * [WordPress](http://wordpress.org/)




The only criteria I used to compare them is the HTTP Headers they sent for the Front Page and RSS Feed.  My theory is that if a blog sends the correct HTTP headers, the coders behind it might have a clue, and it might therefore be better overall software.  Kudos to [OpenSourceCMS.com](http://www.opensourcecms.com) for having Demo sites running for most of the projects.




My rating scale is wrong, unacceptable, acceptable and good. From worst to best:






**Blog::CMS**  

Rating: WRONG  

Lets start with the [front page](http://demo.opensourcecms.com/blogcms/):


Quote from Front Page HTTP Headers:


Generator: BLOG:CMS v3.6.4  

Set-Cookie: lastVisit=deleted; expires=Fri, 02-Jul-04 03:37:19 GMT; path=/  




Generator? huh? Thats not a valid HTTP Header. Yes, you can legally add your own headers, but if you are just making them up, you are supposed to prefix it with 'X-', eg 'X-Generator'.  

  

Next, they did not send any Cache-Control or Vary Headers.  But, they vary the content based on the content of cookies.  This is wrong, and will cause proxies and clients to incorrectly cache pages.  
  

The [RSS Feed](http://demo.opensourcecms.com/blogcms/xml-rss2.php?full=yes) is a little better:


Quote from RSS HTTP Headers:


Pragma: no-cache  

Generator: BLOG:CMS v3.6.4  

Set-Cookie: lastVisit=deleted; expires=Fri, 02-Jul-04 03:38:21 GMT; path=/  

Etag: "503728b580b9894b6aa72317f138cee5"  




The inclusion of an ETag is helpful, but they still send Generator and a Set-Cookie.  The use of the deprecated Pragma header is sad.







**b2evolution**  

Rating: WRONG  

b2evolution doesn't send any headers related to HTTP Caching for the [Front Page](http://demo.opensourcecms.com/b2evolution/index.php?blog=1) or [RSS Feed](http://demo.opensourcecms.com/b2evolution/xmlsrv/rss2.php?blog=1). No ETags, no Last-Modified, No Cookies, nothig, nada. Come on people, this is 2005, not 1997.







**bBlog**  

Rating: Unacceptable  

bBlog does send extra headers, but it sends them attempting to kill all caching on the [Front Page](http://demo.opensourcecms.com/bblog/)


Quote from Front Page HTTP Headers:


Set-Cookie: PHPSESSID=f898e7316af0cd0f4b5e4bcfdc484523; path=/  

Expires: Thu, 19 Nov 1981 08:52:00 GMT  

Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0  

Pragma: no-cache  




Sending an Expires in the extreme past, and forcing all caches to not-cache is lame.  No, I am serious, really really really lame.  HTTP Caching is good, don't try to kill it in all cases, when your frontpage can easily be cached.  
  

Looking at the [RSS Feed](http://demo.opensourcecms.com/bblog/rss.php?ver=2), it is nearly the same story:


Quote from RSS HTTP Headers:


Set-Cookie: PHPSESSID=2978e587e092faa2cd705d7266f3636d; path=/  

Expires: Thu, 19 Nov 1981 08:52:00 GMT  

Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0  

Pragma: no-cache  

Last-Modified: Thu, 02 Jun 2005 23:46:28 GMT  

Etag: ae0a20e9f8140a969c320eb582b62e4b  




They do correctly add a Last-Modified and Etag, but they still are trying to bust the cache.







**Serendipity**  

Rating: Unacceptable  

Similiar to bBlog, Serendipity's [front page](http://blog.s9y.org/) does cache busting:


Quote from Front Page HTTP Headers:


Set-Cookie: PHPSESSID=d6c0446768d6cf4a0aa7c88d6eaba242; path=/  

Expires: Thu, 19 Nov 1981 08:52:00 GMT  

Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0  

Pragma: no-cache  




Ugh. I guess no one really wants the help of HTTP Caching?  
  

At leas the [RSS Feed](http://blog.s9y.org/feeds/index.rss2) is slightly better:


Quote from RSS HTTP Headers:


Expires: Thu, 19 Nov 1981 08:52:00 GMT  

Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0  

Pragma: no-cache  

Last-Modified: Fri, 01 Jul 2005 18:31:42 GMT  

ETag: "Fri, 01 Jul 2005 18:31:42 GMT"  




Okay, Last-Modified, and an ETag, but still sending the Cache Busting stuff.







**Typo**  

Rating: Almost Acceptable  

Typo is the only [Ruby on Rails](http://www.rubyonrails.com/) application I tried, but the [front page](http://blog.leetsoft.com/) isn't very good:


Quote from Front Page HTTP Headers:


Set-Cookie: _session_id=afd0a26b1f95c042e65e34bf2a598a54; path=/  

Cache-Control: no-cache  




Cache Busting. Who has been talking to these Application Developers?  
  

However, the [RSS Feed](http://blog.leetsoft.com/xml/rss/feed.xml) is acceptable:


Quote from RSS HTTP Headers:


Last-Modified: Sat, 02 Jul 2005 03:20:05 GMT  

ETag: "1610900121"  




Last-Modified and an ETag. No cookies.  Pretty good.







**WordPress**  

Rating: Acceptable  

Our first Acceptable entry does not send any related headers on the [Front Page](http://demo.opensourcecms.com/wordpress/), but the [RSS Feed](http://demo.opensourcecms.com/wordpress/?feed=rss2) is good:


Quote from RSS HTTP Headers:


Last-Modified: Sat, 02 Jul 2005 03:26:14 GMT  

ETag: "29f855045e1d4a849c76c24bd8d2406d"  




No Cache Busting, and setup to work with [Conditional Gets](http://www.google.com/url?sa=U&start=1&q=http://fishbowl.pastiche.org/2002/10/21/http_conditional_get_for_rss_hackers&e=10342).







**TextPattern**  

Rating: Acceptable  

Like WordPress, TextPattern didn't send any headers for the [Front Page](http://demo.opensourcecms.com/textpattern/), but the [RSS Feed](http://demo.opensourcecms.com/textpattern/?rss=1) does a perfect job:


Quote from RSS HTTP Headers:


Last-Modified: Mon, 02 May 2005 04:13:50 GMT  

Expires: Sat, 02 Jul 2005 04:42:45 GMT  

ETag: "28AD8AFA-904DDC92"  




Woohoo. Last-Modified, Expires, and an ETag.  Could use a Cache-Control for more specific policies, and I only downgraded it because of nothing sent on the Front Page.







**Conclusion**  

At least a few proejcts get it right for the RSS Feed, but none of them are correct for the Front Page.  I was really disappointed with these results.  I had faith that more people understood HTTP Caching. Is there better software out there?  Have other web developers given up on HTTP Caching?







**Update:** Formating Fixes





**Update 2:** Typo Fixes.



