---
date: '2009-08-20 23:53:53'
layout: post
slug: zfsfreebsd-pain
status: publish
title: zfs+freebsd pain
wordpress_id: '308'
---

Having some fun times with people.apache.org:

    
    minotaur# uname -a
    FreeBSD minotaur.apache.org 7.2-STABLE FreeBSD 7.2-STABLE #0: Wed Aug  5 01:05:27 UTC 2009     root@loki.apache.org:/usr/obj/usr/src/sys/MINOTAUR  amd64
    minotaur# zpool status
      pool: tank
     state: DEGRADED
    status: One or more devices is currently being resilvered.  The pool will
            continue to function, possibly in a degraded state.
    action: Wait for the resilver to complete.
     scrub: resilver in progress for 0h1m, 0.01% done, 266h36m to go
    config:
    
            NAME           STATE     READ WRITE CKSUM
            tank           DEGRADED     0     0     0
              raidz2       DEGRADED     0     0     0
                replacing  DEGRADED     0     0     0
                  da14     UNAVAIL      3   570     0  experienced I/O failures
                  da0      ONLINE       0     0     0  6.24M resilvered
                da1        ONLINE       0     0     0  4.06M resilvered
                da2        ONLINE       0     0     0  4.15M resilvered
                da3        ONLINE       0     0     0  4.09M resilvered
                da4        ONLINE       0     0     0  4.14M resilvered
                da5        ONLINE       0     0     0  4.10M resilvered
                da6        ONLINE       0     0     0  4.15M resilvered
                da7        ONLINE       0     0     0  4.11M resilvered
                da8        ONLINE       0     0     0  4.17M resilvered
                da9        ONLINE       0     0     0  4.08M resilvered
                da10       ONLINE       0     0     0  4.13M resilvered
                da11       ONLINE       0     0     0  4.14M resilvered
                da12       ONLINE       0     0     0  4.14M resilvered
                da13       ONLINE       0     0     0  4.08M resilvered
            spares
              da14         AVAIL   
    
    errors: No known data errors


da14 failed.  we had da0, not in the array yet, so we just did:

    
    zpool replace tank da14 da0


But now it is stuck.

It never makes progress on the Resliver.

It sure sounds like this bug:
[http://bugs.opensolaris.org/view_bug.do?bug_id=6655927
](http://bugs.opensolaris.org/view_bug.do?bug_id=6655927)

But this is FreeBSD 7-STABLE from earlier this month, and it really shouldn't be affected by that bug.

_Sigh._
