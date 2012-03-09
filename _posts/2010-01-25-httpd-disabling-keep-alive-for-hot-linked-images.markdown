---
date: '2010-01-25 19:01:01'
layout: post
slug: httpd-disabling-keep-alive-for-hot-linked-images
status: publish
title: 'httpd: disabling keep alive for hot linked images'
wordpress_id: '321'
---

Lets say you are running a website, and you don't mind people hot linking images, like your Logo, or other resources, and at the same time, you want to enable a (short) Keep Alive timeout for your normal users.

Normal [anti-hot linking recipes, like the one on the HTTPD Wiki](http://wiki.apache.org/httpd/DisableImageHotLinking) are all about disabling access to the image completely.

If you have lots of people hot linking, these users can use up valuable Keep Alive sessions, so the easiest way to solve this problem is to disable Keep Alive for just those clients viewing a hot linked image.

This is possible by using mod_setenvif and the [nokeepalive environment variable](http://httpd.apache.org/docs/2.2/env.html#nokeepalive):


> SetEnvIfNoCase Referer (.+) nokeepalive

SetEnvIfNoCase Referer (.*)example.com(.*) !nokeepalive


What this does is first disable KeepAlive for all users that have a Referer set, and then re-enable keepalive for those users who are coming from 'exmaple.com', which should be replaced with your site.
