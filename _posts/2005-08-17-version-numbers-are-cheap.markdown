---
date: '2005-08-17 20:45:00'
layout: post
slug: version-numbers-are-cheap
status: publish
title: Version Numbers are Cheap
wordpress_id: '92'
---


WordPress recently [released 1.5.2](http://wordpress.org/development/2005/08/one-five-two/).  The problem is that [they modified the release tarballs](http://blog.php-security.org/archives/7-guid.html#extended), after putting the announcement on their site.



Don't do that.  Once you make a version public NEVER change the release tarballs.  It doesn't help that they didn't sign their releases or even provide basic hashes, but the fact that now some users who installed 1.5 2 are still vulnerable, while some others are not is the problem.  This defeats the one major purpose of versioning -- to help the users and admins who install your product.  So they can know if they are vulnerable to an issue.



I am glad that I don't use WordPress, this kind of behavior is not excusable for an Open Source Project.  Its about providing trust to your users.  I can't trust that a WordPress 1.5.2 install is secure, since this one version has two different contents.

