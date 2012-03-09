---
date: '2004-12-05 21:32:45'
layout: post
slug: apr_memcache
status: publish
title: apr_memcache
wordpress_id: '47'
---

[apr_memcache](http://www.apache.org/~pquerna/mc/) is a new client API for [memcached](http://www.danga.com/memcached/).  

Short Example:

    
    
        apr_memcache_t *memcache;
        apr_memcache_server_t *server;
        char* value = "hello world";
        int len;
        ....
        apr_memcache_create(p, 10, 0, &memcache;);
        apr_memcache_server_create(p, "mcache.example.com", 11211, 0, 1, 1, 60, &server;);
        apr_memcache_add_server(memcache, server);
        ....
        apr_memcache_set(memcache, "foo", value, strlen(value), until, 0);
        apr_memcache_getp(memcache, p, "foo", &value;, &len;, NULL);
        printf("result: '%s' len: %d\n", value, len);
    

  

The source code is in [subversion](http://svn.northnitch.com/apr_memcache/trunk/).  I am planning to add it as an [SSLSessionCache](http://httpd.apache.org/docs-2.0/mod/mod_ssl.html#sslsessioncache) backend. [Ian](http://feh.holsman.net/) is already using it in his [mod_ip_bw](http://svn.webperf.org/mod_ip_bw/).  
  

Completely changing pace, the [football game](http://www.carroll.edu/athletics/newsitemview.php?id=1028) on saturday was awesome.  Oh, [dead week is starting](http://www.technicianonline.com/story.php?id=010679). Hurrah.
