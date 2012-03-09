---
date: '2005-03-30 04:08:10'
layout: post
slug: bucket-brigades-are-beautiful
status: publish
title: Bucket Brigades are beautiful
wordpress_id: '63'
---

4 Lines of code to send a segment of a Mailbox file to the browser:


Quote from mod_mbox_file.c:



    
    
        bb = apr_brigade_create(r->pool, r->connection->bucket_alloc);
    
        e = apr_bucket_file_create(f, m->msg_start, m->body_end - m->msg_start,
                                   r->pool,  r->connection->bucket_alloc);
    
        APR_BRIGADE_INSERT_TAIL(bb, e);
    
        return ap_pass_brigade(r->output_filters, bb);
    






Oh. And because of the magic inside httpd, this code will automagically use the file with NMAP for higher performance.  How could it be any easier? 
