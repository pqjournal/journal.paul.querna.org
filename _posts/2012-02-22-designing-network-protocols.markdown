---
date: '2012-02-22 18:24:10'
layout: post
slug: designing-network-protocols
status: publish
title: Designing Network Protocols
wordpress_id: '1106'
---

Hacker News user [peterwwillis](http://news.ycombinator.com/user?id=peterwwillis) started [a discussion about a new network protocol](http://news.ycombinator.com/item?id=3617247) introduced by the [mod_heartbeat](http://httpd.apache.org/docs/2.4/mod/mod_heartbeat.html) module in Apache 2.4:


>It frustrates me when people use ASCII instead of packed bitmaps for things like this (packet transmitted once a second from potentially hundreds or thousands of nodes, that each frontend proxy has to parse into a binary form anyway before using it). Maybe it's a really small amount of CPU but it's just one of many things which could easily be more efficient.



This thread on HN continued with dozens of other posts from many authors, with `peterwwillis` holding his ground on his original point.

I disagree with the belief that a binary format should have been used and will attempt to show why the chosen network protocol for `mod_heartbeat` was both reasonable and correct.



## Background



[Apache 2.4 was released this week](http://mail-archives.apache.org/mod_mbox/httpd-announce/201202.mbox/%3C2922160F-CBF2-4633-8B1E-C5045CC35918%40apache.org%3E), 6 years [after 2.2 was released](http://journal.paul.querna.org/articles/2005/12/02/httpd-2-2-0-released/). Compared to the 2.2 development cycle, where I was the Release Manager, I have not been as active in 2.4. However, one of the few features I did write for 2.4 was the `mod_heartbeat` module.  [mod_heartbeat](http://httpd.apache.org/docs/2.4/mod/mod_heartbeat.html) is a method for distributing server load information via multicast.    While I wrote [mod_heartbeat 3 years ago](http://svn.apache.org/viewvc?view=revision&revision=721952), many other Apache HTTP Server developers have added features and bug fixes since then.


The primary use case is for use by the [mod_lbmethod_heartbeat module](http://httpd.apache.org/docs/2.4/mod/mod_lbmethod_heartbeat.html), to direct traffic to the least loaded server in a reverse proxy pool.

The `mod_heartbeat` code and design was derived from a project at [Joost](http://en.wikipedia.org/wiki/Joost). After stopping development of our thick client and peer to peer systems, we were moving to a HTTP based distribution of video content.   We had a pool of super cheap storage nodes, which liked to die far too often.  We built a system to have the storage nodes heartbeat with what content they had available, and a reverse proxy that would send clients to the correct storage server.


This enabled a low operational overhead around configuration of both our storage nodes and of the reverse proxy.  Operations would just bring on a new storage node, put content on it, and it would automatically begin serving traffic.  If the storage node died, traffic would be directed to other nodes still online.




## Understand your goals



`mod_heartbeat`'s primary goal is: **Enable flexible load balancing for reverse proxy servers**.

For Joost we had good switches since we were previously setup for high packet rate peer to peer traffic.  We also had previously used multicast for other projects.  We choose to use a simple UDP multicast heartbeat as our server communication medium.

When designing the content of this heartbeat packet, I was thinking about the following issues:





  * **10 to 200 servers**: If you only have 10 nodes, you can do everything by hand.  If you have hundreds of nodes, you are most likely building a hierarchical distribution of load.  In my experience it is not a common configuration to have 10,000 application servers behind a single load balancer.  I believe the sweet spot for this automatic configuration via multicast is pools between 10 and 200 servers.


  * **Multiple Implementers**: The Apache HTTP server is all about being the flexible centerpiece of internet architectures, with many diverse producers, consumers, and interfaces.  We must have a network protocol that is easily implemented in any programing language or enviroment, without adding additional dependencies.


  * **Extensibility**: At Joost we embedded the available video content catalogs into the heartbeat advertisements.  We needed a protocol that would be open to proprietary extensions without causing pain.


  * **Limited Network Impact**: In a clustered systems you do not want the overhead of the cluster communication to negatively affect your application.  It is important here to understand that many systems will actually hit [packet-per-second limits before raw bandwidth limits](http://www.cisco.com/web/about/security/intelligence/network_performance_metrics.html).  We also assumed at this point in time all systems have gigabit internal networking.  In my experience the difference between a 20 byte packet and an 8 byte packet that is being multicasted once a second is not a relevant issue on modern LANs. Even with 1000 servers emitting packets, this is 19.53 KB/s of bandwidth. How efficient this network flow is will depend on your exact multicast configuration and your specific switches, but in most configurations it is a non-issue.


  * **Operability / Debug-ability**: [Wireshark](http://www.wireshark.org/) and packet dumps are the best friend of a Network Admin.  When people are doing packet dumps, they are looking for problems.  A simple ASCII encoding of data will be easy for these people to see when they are in times of stress.  Decoding a more complex binary encoding might get added as a feature to Wireshark someday, but it is yet another barrier


  * **Design for the long term**: Design all public network protocols to be around for 10 years or longer.  Include a versioning scheme.  Don't assume that 10 years from now your encoding system will still be around.  I love [msgpack](http://msgpack.org/) for internal applications, but on these time scales for a public protocol, nothing beats straight up ASCII bytes.





## What I did in 2007



Given the above considerations in 2007 at Joost, I started sketching out the possible formats for the multicast packet.

I considered using a binary format, but the immediate problem was having extendable fields.  This meant we would need more than a few simple bytes.  To create an extensible binary format, I started looking at serialization frameworks like [Apache Thrift](http://thrift.apache.org/).  At this time in 2007 [Thrift had only been open sourced a few months](http://blog.facebook.com/blog.php?post=2261927130), and it really wasn't a stable project.  It also didn't have a pure C implementation, and instead would have added a C++ dependency to Apache HTTP server, which is unacceptable.  Since 2007 the number of binary object formats like [BSON](http://bsonspec.org/), [Google Protocol Buffers](http://code.google.com/apis/protocolbuffers/), [Apache Avro](http://avro.apache.org/), and [Msgpack](http://msgpack.org/) have exploded, but just 4 years ago there really weren't any good standardized choices or formats for a pure-C project. The only existing choice would be to use [ASN.1 DER](http://en.wikipedia.org/wiki/ASN.1), which would of implied a large external dependency, in addition to [just being too complex](http://luca.ntop.org/Teaching/Appunti/asn1.html).  I decided that because of this and the other goals around debug-ability to peruse an ASCII based encoding of the content.

The choices for non-binary formats were:





* **XML**: While XML is everywhere, and almost all languages have good bindings, it would be the most verbose choice.  I also felt that it is _too_ extendable.  Someone later would add namespaces and other features that would make implementing a consumer much more difficult.
* **JSON**: Easier to consume, and _today_ there are libraries for all languages.  A major problem was that in 2007, there were no good JSON parsers in pure C.  I know this because at the same time I was working on [libjsox](http://code.google.com/p/libjsox/), a pure C JSON parser with Rici Lake, and it was incomplete. (As an aside, [YAJL is an excellent JSON parsing library](http://lloyd.github.com/yajl/) for C that you should use now days). Like XML, JSON would also mean consumers would potentially have to handle more complex objects, rather than a simple key value pair.
* **Query parameters**: [RFC 3986](http://tools.ietf.org/html/rfc3986
) defined URLs, including the structure of [query parameters](http://en.wikipedia.org/wiki/Query_string). This format is understood by every component in a web server stack, and Apache already included examples of parsing this type of format. The format is also easy to build without external libraries, meaning reimplementation in any language is very easy.  The use of a key and value system also means implementers can use simple data structures like a linked list or hash for interacting with their representation.



I made the decision to use query string style parameters as the best compromise for the content of the multicast packet's content.


In the open source version of `mod_heartbeat`, there are two fields that are exposed today:



* **ready**: The number of worker processes that are ready to accept new connections.
* **busy**: The number of worker processes that currently servicing requests.



Adding the version string `v=1`, and then encoding the fields above we get something like this:


    v=1&ready;=75&busy;=0



## What would I change today?



If I were to need to implement the same system today, there are a few things I might change, but I don't think any of them are critical mistakes given the original design constraints:





* **Consider using Gossip:**  [Gossip based systems are more complex](http://en.wikipedia.org/wiki/Gossip_protocol), but with more and more systems moving to Cloud based infrastructure, multicast communication is not a viable choice.  Additionally, in some infrastructures, multicast can be problematic if not well configured, or if you have too many hosts joining and leaving the multicast group.
* **Consider using JSON**: JSON is a more verbose format, but the availability of parsers in all languages, including C, has significantly improved. I still do not think Thrift or Protocol Buffers are ubiquitous enough to anoint one of them as the only way Apache HTTP Server transports data.





## Conclusion



Binary encodings of information can be both smaller and faster, but sometimes a simple ASCII encoding is sufficient, and should not be overlooked. The decision should consider the real world impact of the choice.  In the last few years we have seen the emergence of Thrift or Protocol Buffers which are great for internal systems communication, but are still questionable when considering protocols implemented by many producers and consumers.  For products like the Apache HTTP server, we also do not want to be encumbered by large dependencies, which rules out many of these projects.  I believe that the choice of ASCII strings, using query string encoded keys and values is an excellent balance for `mod_heartbeat`'s needs, and will stand the test of time.

