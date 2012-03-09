---
date: '2007-07-05 12:11:00'
layout: post
slug: where-is-the-campfire-api
status: publish
title: Where is the Campfire API?
wordpress_id: '196'
---

[Campfire](http://campfirenow.com) seems great.  We have been playing with using it at [work](http://www.bloglines.com/), rather than our internal IRC network, after [seeing this blog post](http://37signals.blogs.com/products/2007/07/web-firm-viget-.html).




The UI is great, the file sharing is great... But the only major blocking issue right now is the complete lack of an API.





Most other 37 signals [apps have official APIs](http://loggedoff.org/articles/2006/07/20/api-projects-for-37signals-applications/), but Campfire only has an unofficial 'API' which is just a [Ruby Module which scrapes the HTML](http://rubyforge.org/projects/tinder).





Look, Ruby is great, but when you are integrating a large project, with existing chat services, you need a standard protocol with good API libraries.  Right now on our IRC channel, we have Bots written in Ruby, Python, TCL, and C/Lua.





They perform all kinds of services, from searching Google, to SVN commit notification, to controlling our [buildbot builds](http://buildbot.sourceforge.net/).





If Campfire at least had some kind of official API, it could be XML based, JSON based, or even something else, I don't really care -- it would allow us to easily port our existing tools in many languages.  Heck, if it had an API, you could also make a [Jabber Gateway easily](http://www.danga.com/djabberd/).





So, here is my request to 37 signals: **I just want an API.**





An API so we can become entrenched into your solution.  So we would never leave.  Right now its a hard sell -- we would be either writing/porting Tinder for 3 or more languages, or investing lots of time in a Ruby based Proxy of some kind, but that all seems excessive. Look at the other 37 signals apps with APIs, a whole ecosystem of things that support your products appear.  APIs are good for you, and good for us, a potential user.
