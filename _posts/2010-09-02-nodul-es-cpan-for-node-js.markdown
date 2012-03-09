---
date: '2010-09-02 09:29:38'
layout: post
slug: nodul-es-cpan-for-node-js
status: publish
title: 'Announcing Nodul.es: CPAN for Node.js'
wordpress_id: '514'
---

Last weekend, our team named "Ponies for Orphans" participated in the [Node Knockout](http://nodeknockout.com/) competition.  The team included 3 of my co-workers from Cloudkick, [Russell](http://russellhaering.com/), [Tomaz](http://www.tomaz-muraus.info/), Logan, and myself. In 48 hours, we had to build a project based on Node.js.

We were brainstorming ideas before the competition, thinking about all the cool things we could do;  We even planned out some multiplayer game ideas.  We quickly figured out that none of us had done anything extensive with Canvas or SVG, and the existing 3rd party libraries aren't very comprehensive, with the possible exception of [Processing.js](http://processingjs.org/). We also felt that we wanted something that would continue to be used after the competition.  We refocused our ideas on projects that would work well with our team composition of being backend programers, and eventually settled on Nodul.es:

Nodul.es: CPAN for Node.js

[Nodul.es](http://nodul.es/) is a web based view of the [NPM package repository](http://github.com/isaacs/npm) for Node.js.  Our goal was simple, implement what we liked about [CPAN for Perl](http://search.cpan.org/) and [Python's PyPi ](http://pypi.python.org/pypi)in 48 hours of coding.

Currently you can browse by:



	
  * [Author](http://nodul.es/authors/)

	
  * [Categories](http://nodul.es/categories/)

	
  * [Alphabetical listing](http://nodul.es/modules/)


Let's look at an example of a module page;  [Tim Smart's node-compress module](http://nodul.es/modules/compress) is a good example.  We pull out metadata from both the NPM repository, the latest commit from Github, and find all modules that have a dependency upon it.


## Internals of Nodul.es


Nodul.es is built around Node.js, using its asynchronous abilities extensively.

We split the system into 3 main components:



	
  * [Indexer](http://github.com/cloudkick/nodul.es/blob/nko-release/lib/services/indexer.js):  Indexes the raw data about packages from the NPM Registry.  This is just a raw JSON dump from NPM's CouchDB backend.

	
  * [Source Downloader](http://github.com/cloudkick/nodul.es/blob/nko-release/lib/services/source_downloader.js): Downloads the latest releases of all NPM modules, and extracts them so we can get extra metadata out about the module.

	
  * [Webapp](http://github.com/cloudkick/nodul.es/blob/nko-release/lib/services/http.js): The _simple_ part, pulls data out of our datastore, and displays html pages to end users.


All of these services interact MongoDB, which provides data storage for all of the indexed data, and ways to get it back out for webpages.

We also used several external dependencies in building Nodul.es:

	
  * [async](http://github.com/caolan/async) - For flow control of asynchronous operations.

	
  * [clutch](http://github.com/clement/clutch) - For URL routing inside the webapp.

	
  * [Mu](http://github.com/raycmorgan/Mu) - For HTML Templating in the webapp.

	
  * [paperboy](http://github.com/felixge/node-paperboy/) - For static file serving (ie, CSS/javascript) in the media subdirectory.

	
  * [prettify](http://code.google.com/p/google-code-prettify/) - For code highlighting, for a feature not released!

	
  * [sprintf](http://www.diveintojavascript.com/projects/sprintf-for-javascript) - For string formatting, in the logs, nice logs are good.




## What's next for Nodul.es


We built Nodul.es in 48 hours, and until the voting is over, we aren't allowed to change it.  But we have a ton of features partially completed that we had to pull because we didn't want to ship broken and incomplete features, they include:



	
  * Source Browser:  We want to provide a similar source browsing experience to CPAN in this respect, letting you quickly see how someone is doing something.  We already have most of the infrastructure for this, because we have downloaded the source tarballs.

	
  * Sitemaps:  We are adding [Sitemaps](http://www.sitemaps.org/), so that all search engines can find the modules easily.  Currently finding modules is an odd combination of using command line tools or getting lucky with a web search.

	
  * More Github integration: The vast majority of Node.js modules are hosted on Github, so we want to do things like show module development activity, and use that to provide sorts on things like Category pages.

	
  * Your ideas: [Nodul.es is open source](http://github.com/cloudkick/nodul.es).  We want to make it the best module browser for any language out there.  Submit Ideas, submit pull requests, lets get going!


