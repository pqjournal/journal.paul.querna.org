---
date: '2005-08-24 19:34:56'
layout: post
slug: ext3-i-hate-you
status: publish
title: ext3, I hate you
wordpress_id: '95'
---


So, my new workstation at work decided today was a good day to stop working.  While I had my full IDE open, it detected journaling errors, and decided to re-mount everything read-only (say goodbye to changes).  Rebooted it, now watching in pain as fsck tells me my filesystem sucks:


> 
Inode 2003227, has a bad extended attribute block 5276170. Clear? yes
  

  
Error reading block 4097088 (Attempt to read block from filsystem resulted in short read) while doing inode scan. Ignore error? yes
  

  
Force rewrite? yes
  

  
`[continue, forever.]`



Running FSCK always sucks.  I wish I could use XFS, but RHEL4 only includes ext3.  Too much pain today. Too much.

