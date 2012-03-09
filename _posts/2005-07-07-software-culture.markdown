---
date: '2005-07-07 13:31:00'
layout: post
slug: software-culture
status: publish
title: Software Culture
wordpress_id: '87'
---


Do you care about the software that you write?



Do you care if it compiles after every commit?  



Are you embarrassed if someone else finds a bug in the code you wrote?



More important than Agile development techniques, is how developers _feel_ about the code.  I view the whole Agile movement, as an attempt to make people care about their code.  To make it embarrassing, if you don't have something to show every two weeks.



Look at the recent PHP exploits from the stupid XML-RPC library.  Ian Bicking goes so far to call [PHP a Ghetto](http://blog.ianbicking.org/php-ghetto.html).  At the end of his post, he talks about the Broken Window Theory.  That visible crap, incites and allows more crap to come.  I won't go so far to call PHP a Ghetto, or the entire language as crap, but it does have an extremely low barrier to entry, and in my experience, the expectations on PHP coders are extremely low.  I have no doubt there is some wonderful PHP code out there, but the culture doesn't innately support it.



I interviewed at Yahoo a few weeks ago, and got to meet [Rasmus Lerdorf ](http://www.google.com/url?sa=U&start=1&q=http://www.lerdorf.com/&e=10342)for the first time in person.  Part of what he does is watch the incoming commits of PHP code at Yahoo, and catch people doing stupid and/or wrong things.  This is actually a really good thing to do.  It should create fear in the PHP coders that work there.  The feeling that they should check their work before they commit, or the guy who invented the language might rant on them.  It is about inducing the same thing Agile Development tries to do.  To make you care about the code.



I believe the [Broken Window Theory](http://en.wikipedia.org/wiki/Broken_Windows) applies to all projects in every programing language.  I consider [Asterisk](http://www.google.com/url?sa=U&start=1&q=http://www.asterisk.org/&e=10342) to have one of the biggest broken windows around.  The entire chan_sip.c file is crap.  But no one cares about adding more crap, and the excuse is that it already sucks, what harm is there in adding one more feature? When you allow crap code to fester, it only makes maintenance harder to deal with.  They still do stupid things with [their Signal Handlers](http://paul.querna.org/journal/articles/2005/02/04/how-to-not-write-a-signal-handler-by-example) too.



A friend works on a $BigProject from a $BigCompany.  They regularly cannot compile their nightly builds, because someone committed code that doesn't even work.  They have lots of other problems, like not having one person responsible for the entire project, but what is most disturbing is the culture that is allowed to persist.   **The culture doesn't mind if the code won't build. ** They are already behind schedule, and I have little hope that they will meet their new shipping date.  I think they need to hire someone to be a culture changer.  Their entire job would be to enforce policies on a daily basis.  Things like, you do not commit code that does not compile.



All of the successful projects I have been involved with have had a culture that does not tolerate stupidity.  Don't use the existing code as an excuse.  It might be crap, but that is never a good reason to add more of the same. 



I try to care.  I hate to commit broken code.  I feel **bad** if I break the build.  Do you?

