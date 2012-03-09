---
date: '2005-02-04 00:18:29'
layout: post
slug: how-to-not-write-a-signal-handler-by-example
status: publish
title: How to not write a Signal Handler... by example
wordpress_id: '53'
---

Read some scary code in [Asterisk](http://asterisk.org/) today:


Quote from Asterisk:
    
    
    static void hup_handler(int num)       
    {                  
            if (option_verbose > 1)
                    printf("Received HUP signal -- Reloading configs\n");
            if (restartnow)
                    execvp(_argv[0], _argv);
            /* XXX This could deadlock XXX */   
            ast_module_reload(NULL);     
    }





1. printf should [not be used in a signal. handler](http://www.freebsd.org/cgi/man.cgi?query=sigaction).  


2. Calling execvp here is completely bogus.  Signals can come at any time, and Asterisk is a multithreaded program. The signal will be handled by a random thread, and this will not do *any* cleanup of the resources used by asterisk.
