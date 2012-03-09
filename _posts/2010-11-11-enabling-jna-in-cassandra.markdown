---
date: '2010-11-11 17:54:02'
layout: post
slug: enabling-jna-in-cassandra
status: publish
title: Enabling JNA in Apache Cassandra 0.6
wordpress_id: '749'
---

## What is it?


[Java Native Access](https://jna.dev.java.net/) is a library to provide access to native function calls on top of the JVM -- from its website:


> JNA provides Java programs easy access to native shared libraries (DLLs on Windows) without writing anything but Java code—no JNI or native code is required. This functionality is comparable to Windows' Platform/Invoke and Python's ctypes. Access is dynamic at runtime without code generation


So, it lets Java easily call functions in a C library, without using JNI or other generated code, just like [Python's CTypes](http://docs.python.org/library/ctypes.html).



## What does JNA do for Apache Cassandra?


Since [Apache Cassandra](http://cassandra.apache.org/) is written in Java, it doesn't have access to many operating system level optimizations, that are helpful when you are building essentially an on disk data storage system.  JNA lets Cassandra access functions that otherwise wouldn't be available in a pure JVM API.

Specific features enabled by JNA in Cassandra:




  * Since 0.6.2: JNA for [mlockall](http://www.freebsd.org/cgi/man.cgi?query=mlockall).  This prevents Linux from swapping out parts of the JVM that aren't accessed frequently.  Chris Goffinet reported a 13% performance improvement in his tests from this change. [CASSANDRA-1214](https://issues.apache.org/jira/browse/CASSANDRA-1214)


  * Since 0.6.6: JNA for hard links, improving snapshots.  Previously Cassandra would use the `/bin/ln` binary to create hard links to SSTables when creating a snapshot.  On nodes with thousands of SSTables, this would take a very long time, because it had to fork+exec the JVM to run the new process.  With JNA, Cassandra uses the [link call directly](http://www.freebsd.org/cgi/man.cgi?query=link&apropos=0&sektion=2&manpath=FreeBSD+8.1-RELEASE&format=html). [CASSANDRA-1371](https://issues.apache.org/jira/browse/CASSANDRA-1371)





## Installing JNA




### Debian & Ubuntu


Debian and Ubuntu have [JNA in their apt repositories](http://packages.debian.org/sid/libjna-java), so in theory it is easy to just install:

    sudo apt-get install libjna-java


However, currently in Ubuntu, it only has version 3.1, while Cassandra wants 3.2.7.  There is a [github here with an updated deb packaging](https://github.com/thepaul/libjna-java) for the most release of JNA, from which you can build your own JNA deb package. If building JNA from source is too much of a pain (and it is, trust me), you can easily grab a binary for it from the [Riptano Debian repository](http://debian.riptano.com/debian/) too.

The deb package will install the JNA jar file to `/usr/share/java/jna.jar`, but Cassandra only loads it if its in the class path.  The easy way to do this is just create a symlink into your Cassandra `lib` directory:

    ln -s /usr/share/java/jna.jar /ck/cassandra/lib/





### Other Platforms


The JNA site has [pre-built binaries that you can download](https://jna.dev.java.net/servlets/ProjectDocumentList?folderID=7408&expandFolder=7408&folderID=0).  On OSX, I just downloaded the .jar file, and then copied it into my cassandra/lib directory for testing.



## Non-Root Operation


If you are not running Cassandra as root, you will need to adjust a ulimit.  The [mlockall system call](http://www.freebsd.org/cgi/man.cgi?query=mlockall) locks pages of memory into RAM which could adversely affect other processes on a machine. For this reason by default there is a 64kb limit on locked memory for most Linux machines.

If you run Cassandra with JNA, and see a log message like this:

    
    Unable to lock JVM memory (ENOMEM). 
    This can result in part of the JVM being swapped out, especially with 
    mmapped I/O enabled. Increase RLIMIT_MEMLOCK or run Cassandra 
    as root.


Then you need to edit the limit.

If Cassandra is the only service on a machine, I suggest just setting the value to unlimited: 

    ulimit -l unlimited


Depending on how you start Cassandra, you might need to add this to your init scripts, so that it is set unlimited before dropping root -- or setup [limits.conf](http://linux.die.net/man/5/limits.conf) for the Cassandra user.



## Verifying


If JNA is working, you will not see a log message about it.  It currently only logs a message if it fails to load or encounters an error.


A special thanks to [Brandon Williams](https://github.com/driftx) on #cassandra for answering all my questions about JNA this afternoon!

