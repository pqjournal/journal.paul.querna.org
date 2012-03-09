---
date: '2010-09-24 05:46:35'
layout: post
slug: cassandra-token-selection
status: publish
title: Cassandra Token Selection
wordpress_id: '550'
---

At a high level [Apache Cassandra](http://cassandra.apache.org/) uses a [hash ring](http://en.wikipedia.org/wiki/Distributed_hash_table) based on a MD5 of the Row Key to determine where the first replica of data lives inside the cluster.  What I am discussing about here is mostly only relevant to the RandomPartitioner. There are many more details about how this works [on the Cassandra Wiki](http://wiki.apache.org/cassandra/Operations).

Each Cassandra node is assigned a token on startup, either automatically via the bootstrap process, or from it's configuration file. If your cluster is always the same number of nodes, you shouldn't need to ever touch these settings.

When you are expanding a cluster, the easiest way is to exactly double the cluster.  When you are doing this, you simply insert each new node half-way in between the old nodes.

When you can't double the size of the cluster, its time to do a little math.

First, lets look at how you calculate the ideal token distribution. Cassandra's ring is from `0` to `2**127` in size.  Using this python function, you can get a list of the ideal intiial tokens for a given cluster size of `n`:


{% highlight python %}
RING_SIZE = 2**127
def tokens(n):
  rv = []
  for x in xrange(n): 
    rv.append(RING_SIZE / n * x)
  return rv
{% endhighlight %}


For example, a 5 node cluster would output values like this:

    
    1:      0
    2:      34028236692093846346337460743176821145
    3:      68056473384187692692674921486353642290
    4:      102084710076281539039012382229530463435
    5:      136112946768375385385349842972707284580



This means the second node in your cluster is responsible from a hash value of 0 to 34028236692093846346337460743176821145.

Since adding new nodes to a Cassandra cluster is an expensive operation, the challenge is to add nodes in the least disruptive manner possible.  This means you want to add nodes in the right places, and then move the existing old nodes with the smallest possible change. (_This isn't strictly speaking true, mostly because of how much the bootstrapping process still sucks, but someday, somewhere over the rainbow, it should be true._)  In Cassandra 0.6.x, the anti-compaction process degrades the node you are taking data from the most, and thankfully this is changed in 0.7.

As a quick hack, I've written a python script which given an arbitrary current cluster size, and any new size, will figure out where you should add nodes, and where you should move your existing nodes to: [cassandra_tokens.py](http://people.apache.org/~pquerna/cassandra_tokens.py).  It works for both growing and shrinking the cluster.

Continuing with the example 5 node cluster above, lets say you want to grow it from 5 nodes to 8 nodes.

This is the output from `cassandra_tokens.py 5 8`:

    [1] Old Node 1 stays at 0
    [2] New Node added at 21267647932558653966460912964485513216
    [3] Old Node 2 moves to 42535295865117307932921825928971026432
    [4] New Node added at 63802943797675961899382738893456539648
    [5] Old Node 3 moves to 85070591730234615865843651857942052864
    [6] Old Node 4 moves to 106338239662793269832304564822427566080
    [7] New Node added at 127605887595351923798765477786913079296
    [8] Old Node 5 moves to 148873535527910577765226390751398592512


On the new nodes, just configure their InitialToken as listed above.  Once they are all bootstrapped, run the `[nodetool](http://wiki.apache.org/cassandra/NodeProbe) move` on the old nodes, one at a time.  This will take quite a long time, since you are going to actually delete your entire set of data on each machine before it is all finished.  Some details about monitoring this process are on the [Streaming Cassandra wiki page](http://wiki.apache.org/cassandra/Streaming), but you will want to get more familiar with [jconsole](http://openjdk.java.net/tools/svc/jconsole/).
