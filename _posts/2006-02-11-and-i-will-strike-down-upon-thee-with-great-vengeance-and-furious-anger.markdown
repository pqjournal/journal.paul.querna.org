---
date: '2006-02-11 02:01:32'
layout: post
slug: and-i-will-strike-down-upon-thee-with-great-vengeance-and-furious-anger
status: publish
title: And I will strike down upon thee with great vengeance and furious anger...
wordpress_id: '124'
---


I have plenty of hate in my heart, but I reserve a special place for websites that create freaking **UGLY** urls.



Today, the [Ask Jeeves Blog](http://blog.ask.com/) did a post on [our new Pisa Office](http://blog.ask.com/2006/02/learning_tower_.html).



They posted some [photos of things going down](http://myjeeves.ask.com/share/showImage?t=fullImage&iurl=http%3A%2F%2Fmyjeeves.ask.com%2Fservlet%2Fsnipit_image_proxy%3Fuid%3D34211032109ec5eae5e1f25ca6e48526%26img_guid%3D499b8b4e5c28d2de7d7c47bf62e56272%26locale%3Den_US&user=sgrieder&path=images+for+sharing&imgid=499b8b4e5c28d2de7d7c47bf62e56272&returl=%2Fpublic%2Fsgrieder%2Ffolders%2Fimages%2Bfor%2Bsharing), and hosted them on [MyJeeves](http://myjeeves.ask.com).  i could do a whole post on MyJeeves, but lets just focus on the URLs that it generates.  Here is the URL it uses to display a single image:



http://myjeeves.ask.com/share/showIm age?t=fullImage&iurl=http%3A%2F %2Fmyjeeves.ask.com%2Fservlet%2Fsni pit_image_proxy%3Fuid%3D34211032109 ec5eae5e1f25ca6e48526%26img_guid%3D 499b8b4e5c28d2de7d7c47bf62e56272%26 locale%3Den_US&user=sgrieder&#3 8;path=images+for+sharing&imgid =499b8b4e5c28d2de7d7c47bf62e56272&# 38;returl=%2Fpublic%2Fsgrieder%2Ffo lders%2Fimages%2Bfor%2Bsharing



The URL is 361 characters long.   There are at least there parameters that look like [some kind of UUID](http://en.wikipedia.org/wiki/UUID).  Why do you need uid, img_guid, and imgid?  I don't care what the technical answer that they might have, its wrong. There are better ways to represent unique resources, and they don't involve multiple unique hashes.



I have only been working at Ask for 6 months now. I want groups inside Ask to choose better URL designs. If you are working on a project, spend a few minutes to think about what the URLs look like. Its really not that hard.



Now, having a URL with 361 characters is pretty bad, but there is one thing **far worse**.  That _thing _is MSN Spaces.  Not only do they use [UUIDs all over](http://spaces.msn.com/chiefskipper/Blog/cns!A59D550BCED8263B!781.entry), they **CHANGE THE URLs OF IMAGES OVER TIME**.  I have heard vaguely that it has something to do with their clustered/distributed filesystem.  Its not really a good excuse to me. Sigh.



The most distributing thing is that these aren't little podunk websites.  These are major corporations, doing major projects, and making some of the worst URL designs ever.



You want to do the right thing?  Go Read [Cool URIs don't change](http://www.w3.org/Provider/Style/URI). Then read [User-Centered URL Design](http://www.adaptivepath.com/publications/essays/archives/000058.php). Good. Now don't write code that creates those ugly URLs ever again.



Remember: _People_ don't make ugly URLs, bad programers do.



**EDIT**: Try to wrap the 361 character URL so it doesn't scroll the entire page.... Arrrg.

