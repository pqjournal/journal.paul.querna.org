---
date: '2005-07-05 15:25:12'
layout: post
slug: response-to-debunking-lighttpd
status: publish
title: Response to Debunking lighttpd.
wordpress_id: '85'
---

The [Debunking lighttpd](http://corelands.com/blog/?postid=82) post has gotten a few harsh comments.  Here are some of my replies.




Quote from Anonymous:


You neglect two things in your discussion: What happens when resources become constrained. For instance what if 10000 slow clients connect to both servers. Which is easier to configure for the task at hand. There are a lot of advantages to using single threaded or tread / core servers. In my opinion this model maps much more closely to the underlying hardware, and many of the problems of multi-threaded systems just don't exist. The market is certainly big enough for multiple players





First point, I don't have a setup to properly test 10,000 slow clients.  If you want to model realistic client connections, then a completely different benchmarking methodology is needed.  ApacheBench is very good at slinging requests in relatively high volume from a single client, but realistic is something that it does not try to be at all.  Someone could write a PHD thesis on realistic modeling of HTTP Clients and Benchmarking.  I don't have the time, the hardware, or willingness to do that right now.


Second point, easier to configure is highly variable based on the administrator experiences.  For me, httpd is easier to configure. YMMV.




Quote from Anonymous:


you make the claim that apache bench sucks, but provide no reasons as to why. You also provide little information about the test itself, results (other than a nice graph), or much information to duplicate the test. I would also be interested in system load at various times during the test too. I would like to say..wow..that is one of the simplest and cleanest apache conf files I have ever seen! :D





ApacheBench Sucks. Why?  It can't scale.  It uses some blocking IO, but tries to use a single/threaded event paradigm. It has no concept of timing.  Its understanding of HTTP/1.1 is limited to KeepAlives. [Justin calls ApacheBench 'dreadful'](http://weblog.erenkrantz.com/weblog/2005/06/05#anandtech-benchmarks). [Flood](http://httpd.apache.org/test/flood/) is a better tool.




To duplicate this test, use the supplied configuration files for both httpd and lighttpd.  Run ApacheBench like so:
`ab -n 10000 -c X -H 'Accept-Encoding: gzip,deflate' -k [http://1.2.3.4/](http://1.2.3.4/)`




I didn't record CPU load during the test.  If you want to spend your time doing it, feel free, I would be happy to point to someone elses more complete benchmarks.





Quote from Anonymous :


Max of 75 concurrency? Since gzip is enabled, you're testing ~13k files with low concurrency, of course Apache does fine. Your test is flawed and your conclusion is misleading.





I only did 75, since both servers were easily maxing out my 100mbit LAN.  If you want realistic testing, you need a very different methodology.  To go to higher, I need better hardware, both for the client machine(s) and for my network. Donations Welcome.




Is my test flawed? On so many levels, yes.  **My argument is that my benchmark is no more flawed than the benchmarks that lighttpd [publishes on their website](http://www.lighttpd.net/benchmark/).**  I actually believe the dataset that I picked was fairly realistic. (enabling gzip+HTML).  I don't think my conclusion is misleading.  Most people are looking for a magical performance pill. I wager most people can get better performance by improving their PHP/scripting code first.



