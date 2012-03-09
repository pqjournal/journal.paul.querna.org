---
date: '2004-11-29 00:50:59'
layout: post
slug: null-termination-attacks
status: publish
title: NULL termination attacks
wordpress_id: '43'
---

For future reference, always remember that [APR Bucket Brigades](http://apr.apache.org/docs/apr-util/group___a_p_r___util___bucket___brigades.html) are not [NULL terminated](http://en.wikipedia.org/wiki/Null_character).  
  

[mod_highlight](http://www.outoforder.cc/projects/apache/mod_highlight/) has had a bug for a couple months now where it would append random binary data to a highlighted file.  I narrowed it down to something inside the `::ParseChunk` function, but it took a week of blanking out at this 10 line function to see this mistake. D'oh.
