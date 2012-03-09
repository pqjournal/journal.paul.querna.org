---
date: '2007-03-20 01:40:00'
layout: post
slug: reinventing-the-wheel
status: publish
title: reinventing the wheel
wordpress_id: '178'
---


So, Imagine you are building a super AJAXy Web 2.0 Application.  And you want to build pretty [REST APIs](http://en.wikipedia.org/wiki/REST), that return [JSON](http://www.json.org/).  Just like all the cool kids are doing.



Lets imagine, to display a view, you need to make 5 different API Calls to load all of the required data.  The standard method is to fire off 5 XMLHTTPRequests (But you are [using dojo.io](http://dojotoolkit.org/intro_to_dojo_io.html), right?).  This doesn't sound that bad, until you consider what the client user agents will do.



The first two requests, A and B, will be sent off in parallel HTTP connections. but the last 3 will wait.  The standard limit for concurent KeepAlive enabled connections per server is 2. They wait until the entire reply of one of the first two is downloaded:


> 
A -> sent to server
  
B -> sent to server
  
... C, D, E waiting
  
A <- finishes
  
C -> sent to server



... D, E waiting


> 
B <- finishes
  
D -> sent to server



... E waiting


> 
C <- finishes
  
E -> sent to server
  
E <- finishes



This means for 5 requests, we are doing a minimum of 3 round trips waiting for the server.



Of course, there is already a way to solve this problem. It is called [HTTP Pipelining](http://en.wikipedia.org/wiki/HTTP_pipelining):



![200703200108](http://journal.paul.querna.org/files/200703200108.jpg)



The problem isn't with the specification, which Apache HTTPD supports, it is that most popular user agents disable HTTP Pipelining.   Even thought Firefox 2.0 supports pipelining, it is [disabled by default](http://www.mozilla.org/support/firefox/tips#oth_pipelining).



This morning over IRC, [Ben](http://blowery.org/blog/) and I came up with an evil alternative.



Rather than complicating our APIs, by building 'combined' object fetches via new APIs, we came up with the idea of multiplexing them generically, allowing any existing API to be used with any others and multiplex them together.



This resulted in [mod_multiget](http://svn.i-want-a-pony.com/repos/mod_multiget/trunk/mod_mutliget.c).



To use it, you just create a request with a POST body of the URLs you want to fetch.  For example if you wanted to fetch data from:




  * /foo/obj/10


  * /foo/obj/15


  * /bar/100




You would create a POST body with:




  * uri_1=/foo/obj/10


  * uri_2=/foo/obj/15


  * uri_3=/bar/100




When you run this against mod_multiget, in a single request, you would receive the content of 3.  It is returned as a JSON object with the following format:



    {
    "requests": [
      {
      "uri": "/foo/obj/10",
      "status": 200,
      "body":  {"id": 10, "data": "foobar"},
      },
      {
      "uri": "/foo/obj/15",
      "status": 200,
      "body":  {"id": 15, "data": "bleh"},
      },
      {
      "uri": "/bar/100",
      "status": 200,
      "body":  {"id": 100, "data": "badgerbadgerbadger"},
      }]
    }

The body block contains the raw data of the different URIs that were requested.



To configure `mod_multiget`, add the following to your httpd.conf:



    LoadModule multiget_module modules/mod_mutliget.so
    <Location /multiget>
      MultiGet on
    </Location>



You can test it with [curl](http://curl.haxx.se/) like this:


    curl -i -d \
    '&uri_1=/foo/obj/10&uri_2=/foo/obj/15&uri_3=/bar/100' \
    'http://localhost/multiget'



A word of warning:  This module does _some evil evil evil stuff_ with Apache Internals.  Sub-requests (which is how this is implemented), where never meant to really be used this way.  This also currently buffers the ENTIRE REPLY in memory.  But it does serve the purpose as prototype.



The cool thing is, this module works with **any** content handler in Apache, so if you are using RoR or Django, or any other method to create JSON, you can bulk the requests using the same module, without any modifications.



The point is, paraphrasing an internal email, this preserves encapsulation of the original APIs, maximizing delegation and allowing for re-use of existing code. This enables the back-end developers to not care about how each small request is multiplexed through this module becuase the access API they export is the same wether or not it goes through the module.

