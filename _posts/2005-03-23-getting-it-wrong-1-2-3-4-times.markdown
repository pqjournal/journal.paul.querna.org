---
date: '2005-03-23 01:22:56'
layout: post
slug: getting-it-wrong-1-2-3-4-times
status: publish
title: Getting it Wrong.. 1.. 2.. 3.. 4 Times.
wordpress_id: '59'
---

The [Apache Tomcat](http://jakarta.apache.org/tomcat/) Connectors are a complete mess.  Here is the list of possible modules to connect HTTPD with Tomcat:


  * mod_jserv

  * mod_jk

  * mod_webapp

  * mod_jk2

  * mod_proxy_http

  * mod_proxy_ajp



**mod_jserv** was the original module.  It is old. I can accept that. Code does get old. Bad ideas are rewritten in new code, but it doesn't fix the fact that the idea is bad. It started the [AJP format](http://httpd.apache.org/docs-2.1/mod/mod_proxy_ajp.html#overviewprotocol) for sending requests around.  
  


**mod_jk** was added in Tomcat 3.x.  It expanded upon the AJP protocol that mod_jserv started with, but I found its configuration to be quite... well, perhaps _crap_ is the best word to describe it.  Oh, and for the win32 binaries, they give you a **.dll** that is named **mod_jk-1.2.8-apache-2.0.52.so**. Yes, your win32 module ends in **.so**.  If you want to support windows users, just make an installer. Its blooody easy. Seriously. Use [NSIS](http://nsis.sourceforge.net/). Oh, mod_jk is also the only remaining connector that should be used 'in production'.  
  


**mod_webapp** was added in Tomcat 4.0(?).  It used the [`WARP/1.0` protocol](http://cvs.apache.org/~jfclere/webapp_docs/warp1.html).  It looks like the protocol didn't add much advantage over AJP, and now its completely dead.  
  


**mod_jk2** was added in Tomcat 4.1(?).  It was a refactor of mod_jk, using [APR](http://apr.apache.org/).  It died a death from lack of developer love.  All the people working on it stopped. Last December, the [Tomcat Team officially dropped 'support' for it](http://jakarta.apache.org/tomcat/tomcat-4.1-doc/jk2/news/20041100.html#20041115.1).  
  


**mod_proxy_http** has been around since httpd 2.0, and it doesn't use some super special optimizaed protocol. It uses plain old HTTP to talk to the Tomcat server.  Is string munging and inserting things into arrays and tables really that slow?  Is there even a need for something like AJP?  
  


**mod_proxy_ajp**, the newest of all these solutions, was added to httpd 2.1.0.  It uses the same AJP protocol as the previous attempts, but instead of writing a proxy module from scratch, it uses the rest of the proxy framework.  
  


Wait a minute. All that every single one of these modules do is **PROXY A REQUEST** to the Tomcat server. Its nothing extra. It only took 5 different Apache Modules and 3 different protocols, and none of them are close to perfect, and none of them are easy to configure.  
  


The FAQ does have [an entry about this](http://jakarta.apache.org/tomcat/faq/connectors.html#vs).
It basically says that mod_jk is the only one that should be used in production.  
  


A different issue that has me worried is how they word [their download page](http://www.eu.apache.org/dist/jakarta/tomcat-connectors/):


Quote:
    
    
    Since November 2004 - <strong>JK2 is officially unsupported!</strong>
    
    JK2 has been put in maintainer mode and no further development will take place.
    
    JK will be fully supported for all relevant web servers.
    


While this sounds simple, I believe it is in psuedo violation of the [Apache 2.0 License](http://www.apache.org/licenses/LICENSE-2.0.html).  My concern is that they are effectively providing a Warranty that **mod_jk** is **fully supported**. Also, Saying that **mod_jk2** will be **officially unsupported** implies that something has **'official support'**.  
  


I have had some of this discussion when I have talked about depreciating httpd 1.3.x.  The reality is that very few developers actively work on 1.3. Yet, it is nneither officially supported or unsupported.  This wishy washy stance hasn't helped with the adoption of 2.0.  I guess one day in a couple years, the 1.3 downloads will be pulled, after [no one has done a commit](http://svn.apache.org/viewcvs.cgi/httpd/httpd/branches/1.3.x/src/CHANGES?rev=156287&view=log) for 5 years.  The simple answer is that an open source project is never dead, but all of the developers can leave, making it quite cold to the touch.  The long answer is that I don't want to deal with Apache 1.3 bugs. Right now, other developers still want to fix bugs in 1.3, good for them. (and for any other unfortunate souls still using 1.3).  
  


Oh. And [Vonage](http://www.vonage.com/) sucks. They are what got me into a grumpy mood today. For the record, they got stuff wrong, **way way way way** more than 4 or 5 times.
