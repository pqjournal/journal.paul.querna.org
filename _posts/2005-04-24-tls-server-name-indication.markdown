---
date: '2005-04-24 21:10:43'
layout: post
slug: tls-server-name-indication
status: publish
title: TLS Server Name Indication.
wordpress_id: '70'
---

I have TLS 1.1 Server Name Indication working in [mod_gnutls](http://www.outoforder.cc/projects/apache/mod_gnutls/).
  
  

What is Server Name Indication?  

When a client connects to a server using SSL, the server will send the Public Certificate to them.  This enables them to actually decrypt the data sent from the server later.  Here is a short simplified example:

    
    1. C: (TLS Handshake) Hello, I support XYZ Encryption.
    2. S: (TLS Handshake) Hi There, Here is my Public Certificate, and lets use this encryption algorithm.
    3. C: (TLS Handshake) Sounds good to me.
    4. C: (Encrypted) HTTP Request
    5. S: (Encrypted) HTTP Reply
    


The problem in HTTP is we don't know which Public Certificate to send, until step 4.  This is long after the public certificate has been sent.  Protocols such as IMAP and SMTP, which use STARTTLS, have a different pattern:

    
    1. C: (Cleartext) I am using server 'mail.example.com'
    2. S: (Cleartext) By The Way, I also support TLS Encryptionn.
    3. C: (Cleartext) Lets use Encryption, aka 'STARTTLS'.
    4. C: (TLS Handshake) Hello, I support XYZ Encryption.
    5. S: (TLS Handshake) Hi There, Here is my Public Certificate, and lets use this encryption algorithm.
    6. C: (TLS Handshake) Sounds good to me.
    7. C & S: (Encrypted) Exchange Data
    


Since the client tells the server which host it is connecting to in step 1, the server can pick the correct certificate in step 5.  It is possible to do this in HTTP, using [TLS Upgrade](http://corelands.com/blog/?postid=51).  This is slightly more complicated, and presents other security issues.  The Server Name Indication approach has a much simplier setup:

    
    1. C: (TLS Handshake) Hello, I support XYZ Encryption, and I am trying to connect to 'site.example.com'.
    2. S: (TLS Handshake) Hi There, Here is my Public Certificate, and lets use this encryption algorithm.
    3. C: (TLS Handshake) Sounds good to me.
    4. C: (Encrypted) HTTP Request
    5. S: (Encrypted) HTTP Reply
    


The only difference is a few extra bytes sent in Step 1.  The client passes along which hostname it wants, and the server now has a clue which public certificate to send.
  
  

Currently, the only browser with SNI support is [Opera 8.0](http://www.opera.com/products/desktop/).  What Server Name Indication (SNI) has the potential to bring, is _cheap encryption_.  A [Self Signed Certificate](http://sial.org/howto/openssl/self-signed/) might be free, but it does not mean they can easily be used.  Other protocols like IMAP use `STARTTLS` to decide which server to connect to first, and then to start the TLS Connection.  Traditionally, HTTP has required one IP address for every SSL Host.  For some people, IP Addresses are cheap, but for many, they are not.  SNI Breaks this last barrier, and allows a single IP Address to host hundreds of SSL Websites.  
  

I have setup a demo server at [sni.corelands.com](https://sni.corelands.com/).  If you visit [https://one.sni.corelands.com/](https://one.sni.corelands.com/) with Opera, you will not get an SSL Hostname Mismatch.  If you use any other browser, you will.
