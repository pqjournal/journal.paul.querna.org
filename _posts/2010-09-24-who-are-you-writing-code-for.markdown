---
date: '2010-09-24 07:44:15'
layout: post
slug: who-are-you-writing-code-for
status: publish
title: Who are you writing code for?
wordpress_id: '542'
---

Brice started a meandering discussion with his post a few weeks ago, [Some random thoughts on programming](http://blog.headspin.com/?p=274), which spawned a lengthy [thread on Reddit](http://www.reddit.com/r/programming/comments/dao05/in_30_years_i_have_only_seen_a_few_examples_where/).

Much of the discussion was focused on "good", "mediocre", "bad" and "terrible" programmers. The problem I have is that the discusion were the comments got bogged down by terminology. Good and bad are moral judgements, assigning an unchangeable label to a person.

I am sure I've been called a terrible programmer by another programmer. And I freely admit, I've written some terrible code;  Though I also think I've also written a decent chunk of 'good' code too.

The problem with evaluating a code base long after it was written, it is very difficult to understand why the code was written, and **who the code was written for**.



# Ask yourself, who are you writing code for today?





## The Deadline.



Perhaps the most common, writing code for a deadline.  Take those short cuts, copy and paste 5 lines rather than refactoring, and just ship it.  We have all done it, and we all knew it was naughty.



## The management metric of great success, extreme edition.



What happens when managers don't understand code, but they have some metric that determines how 'good' a programer is?  Programers figure it out, because they are problem solvers at heart, and optimize for the _game_.  Measuring lines of code, bugs closed, comment density, depth, etc, are all possible indicators of _good_ coders, but by they are all correlations, not causations.  Even more creative metrics like "lines of code removed", will be gamed and your application will be transformed into a [perl one liner](http://sial.org/howto/perl/one-liner/).



## For the Computer.



All programs in some sense must be written for the computer, but perhaps it is the last one you should care about.  Computers care about syntax, they don't care about comments, they don't care about variable names.  Most languages don't care about spacing or code formatting either.  You still must pick the right algorithm, but avoid doing anything to make it faster by micro optimizations.  The choice of `i++` vs `++i` in a for loop is not important, that is what compilers and JITs are for.  Make the code clear and easy to understand before worrying about any micro optimization.  Trust the computer and compilers to be fast for usage common patterns.



## For yourself.



Learning a new programing language is fun, but it isn't ideal if you base your entire companies architecture on it because there was a story about it on [hacker news](http://news.ycombinator.com/), or worse yet, [Lambda the Ultimate](http://lambda-the-ultimate.org/).  When you are writing for yourself, its fine to skip over comments, use bad variable names, write it in 2-space python, and other oddities, but it makes for bizarre code for anyone else to understand.  But its fine, we all need a time and place to _hack_ on something.



## For those who come after you.



Coding is a transference of an abstract idea, into a format that the computer understands.  Writing about abstract ideas is hard for even small things, but many software projects spawn hundreds of thousands or even millions of lines of code, a proper tome of code.   Communicating these ideas to another human being, via a limited syntax in a computer's text file is going to be doomed to failure most of the time.

The best code I've written is where I believe I've spent time to write the comments, outlined the flow of the code, maybe even with some ASCII art diagrams.  Focused on transferring and communicating the idea in my head to whatever unlucky programer soul reads this code later.  But even then, I think by focusing on this communication, the code becomes inhertitly better, because you think more deeply about the abstractions and layering you are doing, instead of just cowboy coding and moving on to the next component.

The act of writing comments makes the code better.  Any time you do something twice, you get better at it the second time.  When you are writing code and comments, you are explaining your abstract problem twice to the reader.  It forces you to think more. Many times I've written the code, then written a comment about it.  Then I go back and rework the code, or even changed simple things like picking better variable names, to better communicate the idea.



## Making a Judgement.


And this is why it is so hard to judge, who is a good and who is a bad programmer.  All these motives are mixed.  When you are evalutating code, it is impossible to know the mindset of the original programmer.  Where they in a rush to leave on Friday for a weekend in Vegas, or was there just an outage in production so they had to put in an emergency hack that stayed there for 5 years?  Or are they just a bad programmer?



## Maybe Programming really is an Art?


I haven't figured judgement out, and I don't think most companies have either.  Look at the interview processes for programers.  They are all over the board on the questions asked;  There is no standard test for computer science students to certify the skills that matter.

There is just too much art in programing to make it just a test or metric.

You know what other field is about communication of abstract ideas to other humans over a visual medium? Art. Paintings. Today we might say that [Van Gogh](http://en.wikipedia.org/wiki/Vincent_van_Gogh) is important and well known as a good artist, but still some people will never like his paintings.  The judgement of good and bad are just too harsh for things that are this abstract, that are really about communication.

The best you can do is remind yourself, and try to code for the right motives.  Avoid coding for the compiler or some management metric. Avoid coding for deadlines, do that little utility function, and document why your code is doing everything.  _You can make the code better, just focus on it, and maybe someone will call you a good programmer in the future, rather than ranting about how terrible your 10,000 line file is!_
