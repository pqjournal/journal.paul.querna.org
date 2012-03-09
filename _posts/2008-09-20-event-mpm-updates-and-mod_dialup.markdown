---
date: '2008-09-20 14:22:33'
layout: post
slug: event-mpm-updates-and-mod_dialup
status: publish
title: Event MPM Updates and mod_dialup
wordpress_id: '231'
---

I know, I know, I haven't written a blog post in months.

Forgive me :-)

Anyways, figured some people might be interested in what I commited last night for the Apache HTTP Server....

First is the ability to 'suspend' an HTTP Request from a Module.

Normally in Apache, there is a one to one relationship between the running thread, and a client connection that it is servicing.  In the [Event MPM previously](http://httpd.apache.org/docs/2.1/mod/event.html), we had broken it out so between different HTTP requests in the same TCP connection, aka Keep Alives, could be serviced by different threads.

Now with [r697357 in httpd trunk](https://svn.apache.org/viewvc?view=rev&revision=697357), you can return SUSPENDED from a content handler.  The core  will assume you have taken over handling of the request, and get out of your way.

This is insanely important, because in the long run it lets you write very cool modules, like a full async HTTP Proxy, aka [something like Varnish](http://varnish.projects.linpro.no/), where you could easily handle tens of thousands of client connections, using only a hundred odd threads, where today you would need a huge amount of RAM, and a single thread or process for every client to do this with Apache.

Secondly, as a demonstration that it works, I wrote [mod_dialup](https://svn.apache.org/repos/asf/httpd/httpd/trunk/modules/test/mod_dialup.c). It is a module that sends static content at a bandwidth rate limit, defined by the various old modem standards. So, you can browse your site with a 56k V.92 modem, by adding something like this:

    <Location /mysite>
        ModemStandard V.92
    </Location>

Previously to do [bandwidth rate limiting modules](http://www.topology.org/src/bwshare/README.html) would have to block an entire thread, for each client, and insert sleeps to slow the bandwidth down.  Using the new suspend feature, a handler can get callback N milliseconds in the future, and it will be invoked by the Event MPM on a different thread, once the timer hits.  From there the handler can continue to send data to the client.
