---
date: '2009-08-23 14:56:53'
layout: post
slug: email-is-awesome
status: publish
title: email is awesome
wordpress_id: '310'
---

my favorite part of [mbox_parse.c](http://svn.apache.org/repos/asf/httpd/mod_mbox/trunk/module-2.0/mbox_parse.c):

    
    
    /**
     * List of all C-T-E Types found on httpd-dev and FreeBSD-current:
     *
     * Content-Transfer-Encoding:      8bit
     * Content-Transfer-Encoding:  7bit
     * Content-Transfer-Encoding: 7BIT
     * Content-Transfer-Encoding: 7Bit
     * Content-Transfer-Encoding: 7bit
     * Content-Transfer-Encoding: 8-bit
     * Content-Transfer-Encoding: 8BIT
     * Content-Transfer-Encoding: 8Bit
     * Content-Transfer-Encoding: 8bit
     * Content-Transfer-Encoding: BASE64
     * Content-Transfer-Encoding: BINARY
     * Content-Transfer-Encoding: Base64
     * Content-Transfer-Encoding: QUOTED-PRINTABLE
     * Content-Transfer-Encoding: Quoted-Printable
     * Content-Transfer-Encoding: base64
     * Content-Transfer-Encoding: binary
     * Content-Transfer-Encoding: none
     * Content-Transfer-Encoding: quoted-printable
     * Content-Transfer-Encoding: x-uuencode
     * Content-Transfer-Encoding:7bit
     * Content-Transfer-Encoding:quoted-printable
     *
     * This is why we have RFCs.
     */
    
