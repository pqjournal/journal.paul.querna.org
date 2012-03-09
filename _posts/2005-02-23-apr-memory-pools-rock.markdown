---
date: '2005-02-23 10:54:00'
layout: post
slug: apr-memory-pools-rock
status: publish
title: APR Memory Pools Rock.
wordpress_id: '54'
---

I was tracking down a memory leak inside HTTPD and got to play with <a href="http://httpd.apache.org/docs-2.0/developer/debugging.html"  class="ng_url">Memory Pool Debugging</a>. In this <a href="http://issues.apache.org/bugzilla/show_bug.cgi?id=33382"  class="ng_url">specific case</a>, Reverse Proxying a Windows Media Server would cause a signifigant leak. This leak was happening while streaming data to the client, so the longer the client was connected, the more memory they used.  
  
I had suspected the bug was in the relatively new and untested mod\_proxy code. mod\_proxy simply hasn't had the same vetting as the core of httpd. I was surprised to find that the bug turned out to be in the <a href="http://lxr.webperf.org/ident.cgi?i=core_input_filter"  class="ng_url">core_input_fitler</a>, far away from the newer Proxy Code. The erroneous use of <a href="http://apr.apache.org/docs/apr-util/group___a_p_r___util___bucket___brigades.html#ga24"  class="ng_url">apr_brigade_split</a> was creating a new bucket brigade every time httpd tried to read data fromt he client.  
  
Now, on to the part where APR memory pools rock. By compiling APR with `--enable-pool-debug=all`, most actions against the memory pool are logged. This includes every allocation, clear or destroying of a Pool. The log includes the size of the Global APR Pool:

Quote from Example Pool Debug Entry:

    POOL DEBUG: [27325/16384] PALLOC ( 244/ 244/ 256702) 0x080A0568 "plog" <strings/apr_strings.c:78> (6/6/1)


By graphing these entries, you can actually see how indiviual apache children act:

[<img width="700" src="http://corelands.com/posts/apr-pools/idle-child.png" />][1]  
The above is a single Idle Apache Child, with just the startup allocations.  
  
[<img width="700" src="http://corelands.com/posts/apr-pools/one-stream.png" />][2]  
This is a Single Streaming Request. Once the Stream is established, we reach a steady state of memory usage.(That is a *good* thing)  
  
[<img width="700" src="http://corelands.com/posts/apr-pools/multi-requests.png" />][3]  
This is a graph of multiple non-streaming requests. Because of how Apache puts the entire connection into a pool, once the client is done, all of the memory used for them can be released.  
  
I made all of the above graphs using a few lines of Python. First I split the `error_log` into one log for every Child using <a href="http://corelands.com/posts/apr-pools/split.py"  class="ng_url">split.py</a>. Then I graphed each using <a href="http://corelands.com/posts/apr-pools/plot.py"  class="ng_url">plot.py</a>.

[1]: http://corelands.com/posts/apr-pools/idle-child.png
[2]: http://corelands.com/posts/apr-pools/one-stream.png
[3]: http://corelands.com/posts/apr-pools/multi-requests.png
