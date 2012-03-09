---
date: '2006-09-14 00:40:00'
layout: post
slug: using-svnsync
status: publish
title: using svnsync
wordpress_id: '163'
---

[Garrett](http://asdf.blogs.com/) helped write svnsync as part of [Subversion 1.4](http://subversion.tigris.org/svn_1.4_releasenotes.html), but I wasn't able to find any documentation for it, other than passing --help.





svnsync is a one way replication system for Subversion.  It allows you to create a read-only replica of a repository over any RA layer (including http, https, svn, svn+ssh).





First, lets setup the initial sync.  We have two repositories, I will skip the details of [svnadmin create](http://svnbook.red-bean.com/nightly/en/svn.reposadmin.create.html). For the remote access to the replica repository, I used [svnserve](http://svnbook.red-bean.com/nightly/en/svn.serverconfig.svnserve.html), and I [added a user with full write access](http://svnbook.red-bean.com/nightly/en/svn.serverconfig.svnserve.html#svn.serverconfig.svnserve.auth.users).  The destination repository should be completely empty before starting.







So, to make this easier, I am going to put the repository URIs into enviroment variables:




    
    
    $ export FROMREPO=svn://svn.example.com/
    $ export TOREPO=svn://dest.example.com/
    





Because the svnsync is allowed to rewrite anything on the TOREPO, we need to [make sure the commit hooks](http://svnbook.red-bean.com/nightly/en/svn.reposadmin.create.html#svn.reposadmin.create.hooks) are configured to allow our 'svnsync' user to do anything it wants.





On the server hosting TOREPO, I ran this:



    
    
    $ echo "#!/bin/sh" > hooks/pre-revprop-change
    $ chmod 755 hooks/pre-revprop-change
    





Now we are ready to setup the sync:




    
    
    $ svnsync init ${TOREPO} ${FROMREPO}
    


This will prompt you for the username, password, and also sets several revision properties on the $TOREPO, for revision zero.  It doesn't actually copy any of the data yet. To list the properties that it created, run:

    
    
    $ svn proplist --revprop -r 0 ${TOREPO}
    
      svn:sync-from-uuid
      svn:sync-last-merged-rev
      svn:date
      svn:sync-from-url
    
    $ svn propget svn:sync-from-url --revprop -r 0 ${TOREPO}
    
      svn://svn.example.com/
    




So all the knowledge about what we are syncing from is stored at the destination repository. No state about this sync is stored in the source repository.





We are now ready to begin copying data:



    
    
    $ svnsync --non-interactive sync ${TOREPO}




And if everything is setup correctly, you will start replicating data.




Except, I suck. And the first thing I did was hit control+c. I figured this is a cool replication system, so I just  ran the `sync` command from above again, and got this:



    
    
    $ svnsync --non-interactive sync ${TOREPO}
    
    Failed to get lock on destination repos, currently held by 'svn.example.com:0e4e0d98-631d-0410-9a00-9320a90920b3'
    Failed to get lock on destination repos, currently held by 'svn.example.com:0e4e0d98-631d-0410-9a00-9320a90920b3'
    Failed to get lock on destination repos, currently held by 'svn.example.com:0e4e0d98-631d-0410-9a00-9320a90920b3'
    Failed to get lock on destination repos, currently held by 'svn.example.com:0e4e0d98-631d-0410-9a00-9320a90920b3'
    Failed to get lock on destination repos, currently held by 'svn.example.com:0e4e0d98-631d-0410-9a00-9320a90920b3'
    Failed to get lock on destination repos, currently held by 'svn.example.com:0e4e0d98-631d-0410-9a00-9320a90920b3'
    Failed to get lock on destination repos, currently held by 'svn.example.com:0e4e0d98-631d-0410-9a00-9320a90920b3'
    Failed to get lock on destination repos, currently held by 'svn.example.com:0e4e0d98-631d-0410-9a00-9320a90920b3'
    Failed to get lock on destination repos, currently held by 'svn.example.com:0e4e0d98-631d-0410-9a00-9320a90920b3'
    Failed to get lock on destination repos, currently held by 'svn.example.com:0e4e0d98-631d-0410-9a00-9320a90920b3'
    svnsync: Couldn't get lock on destination repos after 10 attempts
    




Oh snap.  I guess its not so easy to  restart after an aborted sync.




I started debugging, and found that svnsync kept its lock state in a special property in revision zero again.




So, To fix this, we can safely just delete this lock:



    
    
    $ svn propdelete svn:sync-lock --revprop -r 0  ${TOREPO}
    




Now running `sync` again works! Hurrah!




After the sync finishes, we will want to keep the replica up to date.




I personally set a 'live' sync, but it is also possible to [use a crontab](http://www.freebsd.org/cgi/man.cgi?query=crontab&apropos=0&sektion=0&manpath=FreeBSD+6.1-RELEASE&format=html) or other scheduling method to invoke sync whenever you want.




To setup a live sync, on the FROMREPO server, I appended this to my hooks/post-commit file:




    
    
    svnsync --non-interactive sync svn://dest.example.com/ &
    





You will want to make sure that the user-running subversion (and the hook script) has a cached copy of the authentication info for the destination repository.




Unfortunately, the post-commit hook won't catch everything, so we also need to added this to the `post-revprop-change` hook:

    
    
    svnsync --non-interactive copy-revprops  svn://dest.example.com/ ${REV} &
    




This will help propagate things [like editing svn:log messages](http://subversion.tigris.org/faq.html#change-log-msg).




And there you go, thats the path I took to mirror one of my repositories onto another machine.



