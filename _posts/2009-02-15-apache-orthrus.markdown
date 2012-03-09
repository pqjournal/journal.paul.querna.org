---
date: '2009-02-15 01:42:49'
layout: post
slug: apache-orthrus
status: publish
title: apache orthrus
wordpress_id: '263'
---

If you don't know what [OPIE](http://www.freebsd.org/doc/en/books/handbook/one-time-passwords.html) is, you can likely just stop reading this post now.


> Apache Orthrus is a C library and user interfaces for RFC 2289,
"A One-Time Password System (OTP)", also known as OPIE or S/Key.


SVN: [https://svn.apache.org/repos/asf/labs/orthrus/trunk/](https://svn.apache.org/repos/asf/labs/orthrus/trunk/)

If you have ever tried to compile OPIE on OSX, you might understand why I started this, its just painful and full of silly things.

Most of the Apache Software Foundation's FreeBSD machines use OPIE for our sudo accounts, and I've been using [SkeyCalc](http://www.orange-carb.org/SkeyCalc/), which was last released as a PPC Binary for 10.1 in 2002.  Right now Apache Orthrus can do the _client side_ of OTP, but I want to finish the project to include a PAM module and full verification support.

Patches welcome though, if anyone else uses OTP out there......
