---
date: '2004-06-22 01:20:22'
layout: post
slug: yet-another-project-idea
status: publish
title: Yet Another Project Idea
wordpress_id: '25'
---

I was talking to [Nick](http://www.webthing.com/) on [IRC](irc://irc.freenode.net/apache-modules) today, he has been having some problems with his [gzip inflate filter](http://httpd.apache.org/docs-2.1/mod/mod_deflate.html).  
  



I thought, why not make an 'Apache Filter Debugger'.  The idea is to make a nice Gtk2+ GUI that fakes a request and all structures used by Apache.  It would allow you to set all parts of a request, then specify the input, and a filter chain to run the content through.  After each step you can view the before and after in a multipanel screen, making it easy to see what came in and out.  Just a pipe dream right now, but it could save people hours debuging on [filter modules](http://httpd.apache.org/docs-2.0/filter.html) in Apache 2.  
  


In other news, [ApacheCon 2004](http://www.apachecon.com/2004/US/index.html) has openned with a [Call for Participation](http://www.apachecon.com/2004/US/index.html#cfp).  I am thinking about 3 possible sessions. First up 'XML/XSL and Apache Modules'. I was thinking I could focus on [mod_transform](http://www.outoforder.cc/projects/apache/mod_transform/) and [mod_svn_view](http://www.outoforder.cc/projects/apache/mod_svn_view/) for this session.  My second idea is 'The 2.1/2.2 AAA Framework' where I could take an indepth look at [mod_authn_dbi](http://mod-auth.sf.net), and possibly authentication caching.  My final possible session would be about 'Mass Virtual Hosting in Apache 2.0'.  For this I could combine the work of [mod_vhost_dbi](http://svn.force-elite.com/mod_vhost_dbi/trunk/), [mod_dbi_pool](http://svn.force-elite.com/mod_dbi_pool/trunk/) and [mod_hwshare](http://www.topology.org/src/bwshare/README.html).  I do not know which sessions I want to submit to ApacheCon yet.  I think I will write a small outline for each, then decide which ones to go forward on.
