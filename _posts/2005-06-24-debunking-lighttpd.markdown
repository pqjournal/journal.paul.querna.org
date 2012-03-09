---
date: '2005-06-24 22:50:00'
layout: post
slug: debunking-lighttpd
status: publish
title: Debunking lighttpd.
wordpress_id: '82'
---

[lighttpd](http://www.lighttpd.net/) is a relatively new webserver.  It has quite a few [good features](http://www.lighttpd.net/modules/).  The major design choice, is for it to be completely single threaded and single processed.  This means all dynamic content generation is done via [FastCGI](http://www.lighttpd.net/documentation/fastcgi.html).  
  

On the sidebar, they have a wonderful link to [their _benchmarks_](http://www.lighttpd.net/benchmark/).  Now, we all know that benchmarks are mostly fake, and [ApacheBench](http://httpd.apache.org/docs-2.1/programs/ab.html) is one of the worst available tools for doing benchmarks. They make some great claims on their benchmark page:


Quote from [http://www.lighttpd.net/benchmark/](http://www.lighttpd.net/benchmark/) :


lighttpd + fastcgi is more than 25% faster than apache + mod_php4.  

For **static files** we already know that lighttpd is 4-6 times faster.  

lighttpd is 4-6 times faster in **every setup** than apache and outperfoms thttpd for large files.



(emphasis is mine)  

Well, I can't stand people perpetuating the **myth** that Apache HTTPD is slow. I agree, it will never be the fastest in the world, but is is **not slow**. Therefore, I did some benchmarking of my own.  





**Hardware**  

Client:



Linux 2.6.8-2-k7  

Debian Unstable  

AMD Athlon(tm) XP 1800+  

512 MB RAM  

RTL-8169 Gigabit Ethernet  



  


Server:



FreeBSD 6.0-CURRENT (Custom Kernel, debugging disabled)  

AMD Athlon(tm) XP 1500+   

256 MB RAM  

3C905-TX Fast Etherlink XL PCI 10/100  




  

Both machines are connected to a 24 port 10/100 switch. Nothing super amazing on the hardware size.







**Software**  

lighttpd:



Version: 1.3.14  

Configure Line: ./configure --prefix=/home/chip/bench/lighttpd --with-openssl  

Config File: [lighttpd.conf](http://corelands.com/posts/lighttpd/lighttpd.conf)  




Apache HTTPD:



Version: 2.1.6-alpha  

Configure Line: ./configure --with-mpm=worker --prefix=/home/chip/bench/httpd \  

    --enable-cache=shared --enable-disk-cache=shared \  

    --enable-nonportable-atomics --enable-mods-shared=all \  

    --enable-ssl=shared  

Config File: [httpd.conf](http://corelands.com/posts/lighttpd/httpd.conf)  











**The Test**  

I grabbed a copy of the [Slashdot Frontpage](http://slashdot.org/). 62686 Bytes long.  This file was request 10,000 times at each concurrent client level.  gzip/delfate compression was enabled on both lighttpd and Apache httpd.







**The Graph**  

![](http://corelands.com/posts/lighttpd/graph.png)  








**Insightful Commentary**  

Oh shit. lighttpd isn't faster.  
  

Both servers are able to max out the 100mbit LAN after awhile, but Apache HTTPD got to the point first.  

Will the people who have >= 1 Gigabit Internet Connections to their servers please stand up?  

Yes, you two who pay way too much money, and don't actually use that much bandwidth, you don't count.   

[Yahoo](http://www.yahoo.com) might count, but everyone else sit down.  It doesn't matter which server you use, since both can easily flood your entire maximum outgoing bandwidth.







**Conclusion**  

Changing your webserver doesn't solve real performance issues.  Look at your 200,000 lines of PHP code and slow SQL first.  
  








**Disclaimer**  

Apache httpd had an unfair advantage.  I am an Apache Developer, and breath it every single day.  
  
I have no personal grudge against lighttpd, or it's developers.



  

I don't accept that Apache httpd should be slow, and I don't believe their benchmarks are entirely truthful.  Don't let the myth continue.


**Update 7/05/05:** I replied to several comments [in another post](http://corelands.com/blog/?postid=85).

