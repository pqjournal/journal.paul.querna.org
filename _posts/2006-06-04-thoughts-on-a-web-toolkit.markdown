---
date: '2006-06-04 22:06:21'
layout: post
slug: thoughts-on-a-web-toolkit
status: publish
title: Thoughts on a Web ToolKit
wordpress_id: '142'
---


I have been doing lots of 'Web Development' in C/C++ in the last year.



The current workflow currently isn't that bad, mostly because we use [ClearSilver](http://www.clearsilver.net/) to do many of the hard parts.



Now, ClearSilver is an okay [template language](http://www.clearsilver.net/docs/man_templates.hdf), nothing amazing, but its pretty damn fast, and it works.  However, ClearSilver also includes a "[CGIKit](http://www.clearsilver.net/docs/man_cgi.hdf)" API, which tries to handle many of the hard parts of running a writing a CGI in C.  I would rate the CGIKit as only mediocre, and I have had to dig through it a couple times to extend things or even figure out what the heck it is doing.



I have been thinking about writing a replacement for the CGIKit portion of the API, and using the [Electric Template Language](http://etl.i-want-a-pony.com/) from [Garrett](http://asdf.blogs.com/).



For the API, I am trying to decide between a Monolithic approach, or a more modular one.  A simple question: should the API create the concept of Handlers based on URI prefixes, or should you do that yourself?



For example, if the Toolkit was more Monolithic, you would have an API like this:


> 
pwt_register_handler("/one", one_handler_func);
  
pwt_register_handler("/two" two_handler_func);
  

  
pwt_run_handler();



Which would then call the appropriate function handler if the prefix was matched.



On the other hand, a more modular approach would look like this:


> 
if (pwt_prefix_match(pwt, "/one")) {


> 
one_handler_func(pwt);


> 
}
  
else if (pwt_prefix_match(pwt, "/two")) {



two_handler_func(pwt);



}



Now, the second example is more flexible, allowing you to put hacks in as needed, but it means more code is written.



Of course, now you say, if you design the API correctly, you can do both, and easily degrade into the more modular method when you need that control, which isn't the common case. Right, I have no doubts about that, it just means iterating on the API more before much is finalized, to find those points that need to be able to 'degrade'.



The other challenge in the API design is that I want it to support a CGI mode, FastCGI Mode, and possibly a native Apache Module Handler Mode.  I am pretty sure with some macro-magic that can be done -- and hopefully without hurting either method significantly.



Lastly, I am having an internal debate on if it should be pure-C, or use C++.  I think several parts could be made easier with C++ -- for example you could make you own Classes based off a base PWTHandler and subclass them as needed to your own situation.  I believe many C++ 'libraries' do correctly have a stigma to them -- it is too easy to say, well, i need XYZ, and then just #include boot/foobar.hpp.  And now you depend on [Boost](http://www.boost.org/).  C Libraries have a consistent history in open source of working well. While C++ is exactly the opposite for the most part.  To people who read my blog, do you care which language it is in?  Does either one matter to you?



I have little doubt that all of my goals can be accomplished in straight C, but I think it will end up abusing Macros in ways that I hate to get the lines of code per new handler down to the same number as in C++.

