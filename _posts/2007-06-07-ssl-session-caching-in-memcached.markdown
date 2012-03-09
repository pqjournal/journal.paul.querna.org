---
date: '2007-06-07 21:49:00'
layout: post
slug: ssl-session-caching-in-memcached
status: publish
title: ssl session caching in memcached
wordpress_id: '193'
---

Now in [httpd trunk r545379](http://svn.apache.org/viewvc?view=rev&revision=545379):




`Add support for distributed caching of SSL Sessions inside memcached, using apr_memcache, which is present in APR-Util 1.3/trunk.`




Configure it like this:



    
    
    SSLSessionCache memcache:10.0.0.1,10.0.0.2,10.0.0.3
    




I originally wrote the patch for this back in 2005 at [ApacheCon US](http://apachecon.com/2005/US/).  Never had time to clean it up and  test it... But now we needed it for work.




As with anything using memcache, there is no authentication -- so only use this if your memcache nodes are on a trusted network -- because this could let someone hijack an SSL Session, and that could be _bad_.



