---
date: '2010-01-25 19:09:27'
layout: post
slug: httpd-mod_cache-only-caching-your-homepage
status: publish
title: 'httpd: mod_cache only caching your homepage'
wordpress_id: '323'
---

mod_cache has a pretty inflexible configuration setup.  [CacheEnable](http://httpd.apache.org/docs/2.2/mod/mod_cache.html#cacheenable) can only take a prefix of a path to be cached, and to disable a sub-path with [CacheDisable](http://httpd.apache.org/docs/2.2/mod/mod_cache.html#cachedisable), you need to list all of the possible prefixes (ie, no regular expressions).

Lets say you want to cache just your root page, aka '/', for your website, just in case you get hit by a Slashdot Effect.

For Apache httpd 2.2.12 or newer, you can do this by first enabling Caching on All pages, then setting the [no-cache enviroment variable](http://httpd.apache.org/docs/2.2/env.html#no-cache) globally, and then unsetting it for a specific path:


    CacheDirLevels 2
    CacheDirLength 1
    CacheEnable disk /
    CacheRoot /var/cache/apache2/mod_disk_cache
    CacheIgnoreHeaders Set-Cookie
    CacheIgnoreNoLastMod On
    CacheMaxExpire 600
    SetEnv no-cache
    <LocationMatch "^/$">
    UnsetEnv no-cache
    </LocationMatch>


For Apache httpd before 2.2.12, you need a different method of disabling caching globally, and then re-enabling it.  The easiest way is using [mod_headers](http://httpd.apache.org/docs/2.2/mod/mod_headers.html), to muck with Vary header


    Header set Vary *
    <LocationMatch "^/$">
    Header unset Vary
    </LocationMatch>


Strictly speaking, doing this to the Vary header is an RFC violation, and you best bet is to upgrade to a newer httpd version.  :-)

This works because mod_cache will refuse to cache any HTTP resource with a Vary value of "`*`", because this is saying that every response form the origin will be different.
