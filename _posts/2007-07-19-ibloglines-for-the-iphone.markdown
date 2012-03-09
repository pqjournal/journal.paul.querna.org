---
date: '2007-07-19 20:44:00'
layout: post
slug: ibloglines-for-the-iphone
status: publish
title: iBloglines for the iPhone
wordpress_id: '199'
---

Short: Bloglines Users, go to [i.bloglines.com ](http://i.bloglines.com/) on your iPhone.


![](http://corelands.com/~chip/ibloglines1.png)
![](http://corelands.com/~chip/ibloglines2.png)



[Last Saturday](http://journal.paul.querna.org/articles/2007/07/14/iphone), I got an iPhone.  It was great, but the full size Bloglines on it, with the [Zoom  Mode](http://docs.info.apple.com/article.html?artnum=305899), sucked. Trying to read large volumes of text is a massive pain on the iPhone.





On Sunday morning, I started working on an iPhone specific site for Bloglines.  By mid-afternoon on Sunday, I had something that worked reasonably well.






I spent the rest of this week taking in refinements and new feature suggestions from everyone inside the company.





Thanks to everyone on the Bloglines team for helping out with this project. It is by far the coolest thing we have released this year so far.






The iBloglines site is written with:






 
  * 253 lines of C++ in 5 files

 
  * 382 lines of client side Javascript in 1 file

 
  * 287 lines of ETL Templates in 8 files





Of course, this is only counting the code we wrote specifically for the iPhone, but it does make me doubt that you need to use a Scripting Langauge for rapid development, if your framework is good enough.






iBloglines is built upon [iUI](http://joehewitt.com/iui/) .  Originally we tried to just using it as a base, but in the end, we essentially forked it. We entertained using [Dojo 0.9](http://dojotoolkit.org/) on the iPhone, but since the only required browser to support is MobileSafari, it would of been pretty heavy.






We used [The Electric Template Language](http://etl.i-want-a-pony.com/), or ETL for generating the HTML.  Relatively young compared to things like [ClearSilver](http://www.clearsilver.net/), it is much cleaner and was a joy to work with.






Developing for the iPhone has been pretty fun, but I believe Apple has been less helpful that they should be.  






**We might not need a SDK for 'native' Applications,
but we need better tools for the iPhone.**





Simple things, like making an official iPhone Simulator, like Microsoft has [for Windows Mobile](http://msdn2.microsoft.com/en-us/windowsmobile/bb264327.aspx), which had identical rendering to the iPhone would be very helpful. [iPhoney](http://www.marketcircle.com/iphoney/) is a good start, but it really should be an official Apple Developer tool.





We did most of our development on Firefox with [Firebug](http://www.getfirebug.com/), and then ported it to the MobileSafari later, because the tools for Firefox are so much better.





In closing: I love my iPhone, I hope Apple will hurry up and make better developer tools, and I hope the Bloglines users enjoy the new [iBloglines](http://i.bloglines.com/)!



