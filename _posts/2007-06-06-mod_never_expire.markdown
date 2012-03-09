---
date: '2007-06-06 00:18:00'
layout: post
slug: mod_never_expire
status: publish
title: mod_never_expire
wordpress_id: '192'
---

Remember [mod_images_never_expire](http://use.perl.org/~geoff/journal/22049)?





Well Today I wrote [mod_never_expire](http://people.apache.org/~pquerna/modules/mod_never_expire.c) . Its pretty much the same idea, but its a little more configurable, and for files it sets long expire and cache-control headers.... And it works in httpd 2.x




To use, you just use any Directory/Location/Files container, and tur it on:



    
    
      <LocationMatch ^/c/css/r\d+/.+\.css>
        NeverExpire on
      </LocationMatch>
    




or:

    
    
      <Directory "/foo/bar/js/">
        NeverExpire on
      </Directory>
    





Great for Images, CSS, and Javascript, as long as you properly version your URLs.

