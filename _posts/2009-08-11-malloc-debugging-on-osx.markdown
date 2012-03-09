---
date: '2009-08-11 13:05:15'
layout: post
slug: malloc-debugging-on-osx
status: publish
title: malloc debugging on OSX
wordpress_id: '299'
---

I can never remember all of the options for [malloc(3)](http://developer.apple.com/documentation/Darwin/Reference/ManPages/man3/malloc.3.html) on OSX when debugging.  So I'm posting it here so I can find it with Google Search next time I need to find it:
`
export MallocLogFile=/tmp/malloc.log
export MallocGuardEdges=1
export MallocStackLogging=1
export MallocStackLoggingNoCompact=1
export MallocPreScribble=1
export MallocScribble=1
export MallocCheckHeapAbort=1
export MallocBadFreeAbort=1
ulimit -c unlimited
`

similar malloc debugging for linux:
`
MALLOC_TRACE=/tmp/out.log
`
related: [memcheck](http://www.gnu.org/s/libc/manual/html_node/Heap-Consistency-Checking.html).
and [more info on the suse wiki](http://en.opensuse.org/SDB:Debugging_with_Glibc#Debugging_Malloc-related_problems).
