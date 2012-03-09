---
date: '2005-04-09 00:46:04'
layout: post
slug: forcing-a-kernel-panic
status: publish
title: Forcing a Kernel Panic
wordpress_id: '67'
---

Ever Wondered how to panic a Linux Kernel?  It is really easy.  Here is your source code:


Quote from panic.c:
    
    
    #define __NO_VERSION__
    #include <linux/version.h>
    #include <linux/kernel.h>
    #include <linux/module.h>
    
    int init_module(void)
    {
        panic(" insert lame excuse here");
        return 0;
    }
    






Then compile it with `gcc -I/usr/src/linux/include -D__KERNEL__ -DMODULE -o panic.o -c panic.c`.  

Now just run `insmod panic.o`. 

  
  
Okay, So I was a little bored tonight.
