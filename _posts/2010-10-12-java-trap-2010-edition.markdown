---
date: '2010-10-12 03:18:18'
layout: post
slug: java-trap-2010-edition
status: publish
title: Java Trap, 2010 Edition
wordpress_id: '656'
---

As a member of the [Apache Software Foundation](http://www.apache.org/), my views on open source tend to gravitate towards more liberal licenses, like the [Apache License (v2.0)](http://www.apache.org/licenses/LICENSE-2.0), BSD, or MIT licenses.  I strongly believe in enabling companies to take open source software and do whatever they wish to do with it, placing as little restrictions as feasible under current laws.  I believe that better communities for software development are enabled by these liberal licensing situations. Rather than creating a single power with significantly more rights, as seen in the ["open core" movement](http://blogs.gartner.com/brian_prentice/2010/03/31/open-core-the-emperors-new-clothes/), liberal open source development encourages real, dedicated and sustainable contributions, made by companies with business models other than selling support and 'enterprise features'.

I have to be honest -- I am not a huge fan of Java the language -- I would rather write code in Python, Javascript, C, C++, or heck maybe even PHP, but I find myself surrounded by Java everywhere.  Java and the JVM today are core to many components we are using to build [Cloudkick](http://www.cloudkick.com/), and there are no viable alternatives.

Today IBM announced they are shifting their focus, and will be [developing on top of the OpenJDK](http://www.sutor.com/c/2010/10/ibm-joins-the-openjdk-community/).  This comes in addition to the [Oracle lawsuit against Google over Android](http://www.groklaw.net/article.php?story=20101005114201136). Oracle is good at big company politics, and at extracting value -- I'm sure they will extract every penny out of Sun's husk.

While Sun, now Oracle, has licensed the OpenJDK itself under the GPL, the licensing of the TCK has been a problem for [more than 5 years](http://www.apache.org/jcp/sunopenletter.html).  Other blog posts go into far more detail about this [1](http://www.redmonk.com/jgovernor/2010/10/01/java-the-unipolar-moment-on-distributed-governance-for-distributed-software/) [2](http://www.readwriteweb.com/archives/google_invokes_history_of_java_responds_to_oracle.php) [3](http://www.h-online.com/open/news/item/Apache-votes-no-on-Java-EE-6-740359.html), and I encourage you to understand all the details about the story of the TCK, Apache, and Sun -- but it isn't what I want to focus on.

I consider myself an open source advocate, though in a far different manner than someone like [Richard Stallman](http://en.wikipedia.org/wiki/Richard_Stallman), creator of the GNU Project.  Richard's views and my own don't often align around many topics, but the increasing turmoil in the Java world has changed some beliefs I have about software platforms and licensing.

More than 6 years ago, "[Free but Shackled - The Java Trap](http://www.gnu.org/philosophy/java-trap.html)" was published by Richard.  While I don't agree with the moral arguments about the freedom of software, I now believe that the Java platform is a trap.

Richard speaks about the Free World, and many other GNU priorities in this excerpt, but I believe the core point is the most important. If your code depends on a platform, you are at the mercy of that platforms licensing and development:


> This problem can occur in any kind of software, in any language. For instance, a free program that only runs on Microsoft Windows is clearly useless in the Free World. But software that runs on GNU/Linux can also be useless if it depends on other nonfree software. In the past, Motif (before we had LessTif) and Qt (before its developers made it free software) were major causes of this problem. Most 3D video cards work fully only with nonfree drivers, which also cause this problem. But the major source of this problem today is Java, because people who write free software often feel Java is sexy. Blinded by their attraction to the language, they overlook the issue of dependencies and fall into the Java Trap.



**When you build software in Java and the JVM, you are being locked into only running it on a platform controlled by a single company -- Oracle.**  Oracle is working to maintain this platform control by refusing to remove the field of use clauses in the TCK, effectively preventing Apache Harmony from ever being able to ship a real release.  The lawsuit against Google also confirms the fear of Oracle using their control of the platform aggressively.

The problem is not so much about Oracle controlling their code.  As I said above, I believe in the rights of a company to do as these choose -- but at the same time, if they choose to be bad stewards of this, I will choose not to use their platform.  Most importantly in the Java world, is that stranglehold being placed upon 3rd party implementations.   Oracle could close source the OpenJDK for all I care, but what offends me most is their desire to squash alternatives implementations.

Consider some alternatives to Java, which all have multiple implementations now:




  * **Python:** CPython, but also has PyPy, IronPython, and Jython.


  * **Ruby:** MRI, but also JRuby, MacRuby, 

  * **Javascript:** v8 (node.js), Spidermonkey, whatever-safari-is-calling-their-JS-engine-now.


  * **C/C++:** Clang and GCC


  * **C#:** CLI and Mono



These multiple implementations of the languages are creating innovation on their respective platforms.  They are all for the most part driven by diverse communities, mostly under liberal licenses.  Communities built around common goals and beliefs, rather than arcane licensing policies trying to protect a company's mobile market.  In Java you will only be given one choice, the choice that Larry and Oracle give you. Any attempts to build an alternative implementation will be made exceedingly difficult.

When I am picking a platform to build upon, I want to know it will be around regardless of the whims of a single company.  I want to know there is a diverse community behind it.  I want people to be experimenting with new ways to build a VM to make the platform even better.

This is why I must ask, how can anyone pick Java and the JVM on which to build their company's future?  I know Oracle and IBM -- they will pump millions into the continued development of the platform, but it's not a platform I want to be using.  Big companies throwing around development like this don't create the values I find essential in picking a platform.  Oracle is going to control the future of Java.  I don't know what will happen to the [Java Community Process](http://en.wikipedia.org/wiki/Java_Community_Process), but I lack any faith in it continuing.

Take a hard look at your development, why are you using Java?   Are you building upon a platform where open experimentation is encouraged, and not feared?  It is impossible for a business to pivot and abandon Java in a day, but after the events of the last few months, I will seek to use alternatives wherever possible.

**Is your platform free, or is it a trap?**
