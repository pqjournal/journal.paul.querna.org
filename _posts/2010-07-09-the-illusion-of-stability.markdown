---
date: '2010-07-09 00:03:15'
layout: post
slug: the-illusion-of-stability
status: publish
title: The Illusion of Stability
wordpress_id: '389'
---

Back at the [May 2010 Board meeting of the Apache Software Foundation](http://www.apache.org/foundation/records/minutes/2010/board_minutes_2010_05_19.txt), there was a discussion about releases.  It got me thinking about how my own use of many open source projects has changed.

**The Past - Long Cycles, few releases, software ships on physical media**

[Myst](http://en.wikipedia.org/wiki/Myst) pushed the limits by being shipped on a CD-ROM instead of floppy disks, and [Riven](http://en.wikipedia.org/wiki/Riven) followed with pushing the adoption of DVDs by shipping on 1 DVD, or 5 CDs.  Physical media kept accelerating to a point, now days most software can be downloaded.  Even for game consoles, previously one of the last barriers for things like patches, games like Call of Duty: Modern Warfare 2 have a half dozen post-[gold master](http://en.wikipedia.org/wiki/Gold_master) patches, pushed down to internet connected consoles.

If you look at the development of software over the last 20 years, one of biggest changes for many products is the shift in distribution, lots of people talk about Software as a Service, but really you need to just look at software on desktops -- products like Google Chrome automatically apply updates without bothering the user, and most products ship with an auto-update mechanism at a minimum.

But the fundamental difference in this is a shift in the software development and release models, that the software distribution systems have finally caught up to.

**Release Cycles**

I view Ubuntu as one of the first large projects to recognize this shift and embrace it.  Many large-scale projects in the mid-2000s had massive problems tracking dependencies, and synchronizing anything resembling a stable final product was a challenge.  [Ubuntu's model of picking a date](https://wiki.ubuntu.com/TimeBasedReleases), and shipping whatever was stable at that point shifted the responsibility model for stability.  Other projects have done this before Ubuntu, but Ubuntu has stuck to it and exposed so many more people to the model.  Every 6 months, Ubuntu drew a line in the sand, and whatever was stable before that date, became the next Ubuntu release.

This meant, you didn't just wait for the new release of GNOME or KDE and then try to stabilize everything;  You certainly hoped for dependencies to add new features before your dates, but if they missed it, they would go into the next release.  Compare this to the traditional Linux distribution: multiple rounds of betas to squash out all the integration pain of bringing together thousands of dependencies into a stable final product.

**But I don't make a Linux distribution! **

Most  software projects I've worked on have had large dependencies on Open Source Software.  Not thousands of projects like a Linux distribution. Some only had a few dependencies. Others had a few dozen projects that they were directly built on top of.  In the past, you took a recent stable release and built packages of it or pulled it into a [vendor branch](http://svnbook.red-bean.com/en/1.5/svn.advanced.vendorbr.html).  There was an expectation that releases were... Stable and would get maintenance patches for serious bugs.

At [Bloglines](http://en.wikipedia.org/wiki/Bloglines), the product was built on top of 30+ open source projects, from [BerkeleyDB](http://www.oracle.com/technology/products/berkeley-db/index.html), to [libcurl](http://curl.haxx.se/libcurl/),  to [Clearsilver](http://www.clearsilver.net/).  We tried to take the stable releases, and knit it all together into something that worked. For the most part we were successful.  However, we patched lots of projects, some of them were patches we pushed upstream, others were Bloglines specific modifications, but we thought it was okay, we were taking stable version of Foo, and appling a few patches.  We knew upgrading to the next version of Foo might be painful, but there normally was documentation explaining what changed.

**The End of releases**

But what the Apache Board meeting got me thinking about, was our dependencies at [Cloudkick](https://www.cloudkick.com/).  We use a ton of Python at Cloudkick, a few projects like [Twisted](http://twistedmatrix.com/trac/), and [Python](http://www.python.org/) itself, we generally use a stable release, and its fine and dandy.  But for many of our more esoteric dependencies like [txAMQP](https://launchpad.net/txamqp), [libcloud](http://incubator.apache.org/libcloud/), [scribe](http://github.com/facebook/scribe), a few [Django](http://www.djangoproject.com/) applications, oauth, sales force libraries, etc, we are using snapshots, mostly from someone's GitHub repository.

I am grateful for the projects we build on, and we try to contribute back to them whenever we can, but it is no longer taking a stable release and making a few local modifications -- we are lucky if a project has releases at all, let alone stable releases!

I don't think its the fault of things like GitHub, they have download areas, and some projects use them, but the majority don't.  They give you a git url, and its up to you to pick a 'stable' point in time, and hope for the best.

**What did those releases provide anyways?**

On some levels, I miss stable releases.  It made me feel good, it let me judge at face value, some programer I probably will never meet in person felt good enough about some code, to call it 'stable'.    But the reality was, any code I've pushed hard, I've found bugs, and then I patched those bugs or added new features.

Code that wasn't pushed hard, it probably didn't matter if someone else thought it was stable, it was good or bad, it worked or it didn't.

Those releases from someone else provided me with the illusion of a stable product. Something I can build upon;  But the truth when I look hard at the projects I thought were stable, we ended up patching some of those the most!

This newer age paradigms for software releases mean you can move unbeilievability quickly, bringing together diverse peices of software and building communities around new software faster than ever.  I look at the [Node.JS modules page](http://wiki.github.com/ry/node/modules),  and I'm blown away.  There are many projects that probally should be added to that list, many removed, but the sheer number of projects, most of them only a few months old, exploding in popularity, its all enabled because the expectations for an open source product have changed.

You no longer wait for the once a year stable release of any dependency, you grab the snapshot from GitHub, find the author on IRC or twitter if there is a problem, patch it locally, submit a pull request, and then keep on building your product.

This model does bring other problems, many of them core to traditional thought at the Apache Software Foundation. Code pulled from SVN trunk aren't vetted in the same way at the ASF.  Many of the younger ASF projects have had more trouble making releases, and this is difficult for the slow moving foundation to always understand why releases are not a higher priority.  I believe this lack of stable products definitely has hurt the Ruby/Rails community in the last few years too.

We should embrace this change. We are all developing software at breakneck speeds. Software has always been unstable, nowadays we are just honest enough to admit it. What we need is better tooling, not just a distributed version control, but more on the deployment and packaging side for most web applications. The tools have not caught up to changes in development and dependency philosophy, when most sites are still deployed with some variation of a hacked together shell script.

-----------------------

Thanks to [Geoff](http://geoff.greer.fm/) for giving feedback on this post.
