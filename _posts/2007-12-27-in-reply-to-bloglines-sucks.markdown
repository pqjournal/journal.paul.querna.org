---
date: '2007-12-27 21:52:34'
layout: post
slug: in-reply-to-bloglines-sucks
status: publish
title: in reply to "bloglines sucks"
wordpress_id: '221'
---

In reply to Scoble's post today, "[Bloglines Sucks](http://scobleizer.com/2007/12/27/bloglines-sucks-2/)".....

I will first try to outline the "issue".

At the bottom of every post on a wordpress.com blog, is a tracker image used for statistics.  It includes a rand parameter, which changes every time the feed is fetched over HTTP.  The image URL is something like this:


> http://stats.wordpress.com/b.gif?host=scobleizer.com&rand=2045631674&blog=3428&post=3957&subd=scobleizer&ref=&feed=1


Because this rand value changes every time we read the feed, we considered the Item '**Updated**'.

The behavior of the last 40 posts being shown as updated, every time a new post was added was caused by our use of the [HTTP ETags and Last-Modified features](http://fishbowl.pastiche.org/2002/10/21/http_conditional_get_for_rss_hackers).  Since Wordpress.com returns a 304 Not Modified for most of our crawls, we would only 'reparse' the entire feed when a new post was added.

Now, The reason users do not see this _problem _in Google Reader, is that Google Reader has no concept of an "**Updated**" item. When a writer edits a blog post later, users in Google Reader would never see the changes.  In Bloglines, we have always considered this a feature, showing you the user when a blog post is edited.

In Bloglines you can disable this feature, on a per-feed basis:


> In [Bloglines Beta](http://beta.bloglines.com/), click on the feed, then select Edit.  Change the "Updated Items:" to "Ignore".

In Bloglines Classic, click on the feed, then select edit subscription.  Change the "Updated Items:" to "Ignore".


As far as I can tell, the use of a rand parameter in the Wordpress.com statistics image is a new change, also introduced at the same time the inline comment images were added to feeds.

[FeedBurner](http://www.feedburner.com) includes similar statistics, tracking images and comment images, but they do not include a constantly changing image url.  This works correctly in Bloglines.

In regards to placing blame, [Dana Epp says "Bloglines says it's not them"](http://silverstr.ufies.org/blog/archives/001029.html).  I don't know who Dana has talked to inside Bloglines. When these type of issues are reported, we generally try to get in touch and investigate with the publisher, and hopefully figure out what is going on together, rather than outright saying its not our fault.  It is a bad experience for our users, and we always want to be involved and help fix it.

I first heard about this issue on Friday, December 21st from [Matt](http://photomatt.net/) via email. (also [my birthday](http://journal.paul.querna.org/articles/2007/12/21/22-23/))  I forwarded that email onto our internal Bloglines Engineering Mailing list, but frankly, I didn't expect anyone to work on the issue on the Friday before Christmas.  [IAC Search and Media](http://sp.ask.com/en/docs/about/company_overview.shtml), the parent company of Bloglines and Ask.com, also has a mandatory Holiday Shutdown this week for all employees.  No one will be in the office officially until January 2nd, 2008.

Luckily or unlucky, depending on your perspective, I took some time this afternoon away from my family to read my feeds.  For now the bug^H^H^Hfeature in Bloglines of showing edited posts has been fixed.  I've have simply turned it off for all users.

I hope you had a Merry Christmas, and have a Happy New Year.
