---
date: '2010-07-10 11:50:05'
layout: post
slug: overclocking-mod_ssl
status: publish
title: Overclocking mod_ssl
wordpress_id: '422'
---

At Velocity, I saw Adam Langley give a great presentation entitled [Overclocking SSL](http://en.oreilly.com/velocity2010/public/schedule/detail/14217).   Last week Adam posted a distilled version of the [Overclocking SSL presentation on his blog](http://www.imperialviolet.org/2010/06/25/overclocking-ssl.html).

He covers many topics for improving SSL performance. Unfortunately, his recommendations are decidedly focused on how Google runs their servers, and not a practical guide to how to improve your performance with a more standard Apache 2 and mod_ssl setup.  Since I don't work at Google, but I like my web servers to be fast, I decided to try as many of his recommendations as possible with mod_ssl.

_Disclaimer_ I am not a cryptanalyst.  Be paranoid when you are messing with SSL, small mistakes can invalidate your entire security framework.  Ask your local cryptanalyst about these changes!



## Basic Configuration: Certificate Key Size


Google uses a 1024bit RSA key for their encrypted websites.  However, Certificate Authorities are no longer issuing new 1024 bit keys, because the [CAB Forum has required them to be phased out at all levels](http://www.entrust.net/knowledge-base/technote.cfm?tn=7710).  It is believed these small keys are insecure, so for pratical purposes this means you will want a 2048bit key.  Make sure you do not use a 4096 bit key, the key operations are about 5 times slower -- make sure you have a 2048bit key, it strikes the balance of speed and security.

The Certificate key sizes doesn't just affect how many CPU cycles that are used for the calculations, the public versions of the keys are sent to the client when it connects. I go into more detail about TCP round trips bellow, but if your certificate is a 4096 bit key, it means your clients need to download double the data to even get started.



## Basic Configuration: Picking Ciphers


The [SSLCipherSuite directive](http://httpd.apache.org/docs/2.2/mod/mod_ssl.html#sslciphersuite) controls the ciphers that mod_ssl will negotiate with clients.  The string parameter is complicated -- it is a combination of aliases of 'HIGH', "LOW", old names, specific names, etc.    To see what OpenSSL actually enables, you'll want to use the `openssl ciphers` command.

This is what you get for the default configuration of mod_ssl:


    $ openssl ciphers 'ALL:!ADH:RC4+RSA:+HIGH:+MEDIUM:+LOW:+SSLv2:+EXP'
    
    DHE-RSA-AES256-SHA:DHE-DSS-AES256-SHA:AES256-SHA:DHE-RSA-AES128-SHA:
    DHE-DSS-AES128-SHA:AES128-SHA:EDH-RSA-DES-CBC3-SHA:EDH-DSS-DES-CBC3-SHA:
    DES-CBC3-SHA:DHE-RSA-SEED-SHA:DHE-DSS-SEED-SHA:SEED-SHA:RC4-SHA:RC4-MD5:
    EDH-RSA-DES-CBC-SHA:EDH-DSS-DES-CBC-SHA:DES-CBC-SHA:DES-CBC3-MD5:
    RC2-CBC-MD5:RC4-MD5:DES-CBC-MD5:EXP-EDH-RSA-DES-CBC-SHA:
    EXP-EDH-DSS-DES-CBC-SHA:EXP-DES-CBC-SHA:EXP-RC2-CBC-MD5:EXP-RC4-MD5:
    EXP-RC2-CBC-MD5:EXP-RC4-MD5


The exact list will depend upon your version of OpenSSL, but on most modern operating systems, the first cipher that will be attempted to be used is AES-256.  AES-256 is without a doubt a more secure selection, but it isn't what Google is using.  They are using the older [RC4 (aka ARC4)](http://en.wikipedia.org/wiki/RC4) cipher, with SHA1 hashing.  There have been many different attacks on RC4, many due to bad implementations, but as long as it is used correctly, it is still _secure enough_.  The selection of a cipher is still a judgement call for your product, but RC4 is approximately 3x faster than AES-256 on most machines right now.

In Apache, lets configure it to try to use RC4 w/ SHA1 hashing:

    
    SSLCipherSuite RC4-SHA:AES128-SHA:ALL:!ADH:!EXP:!LOW:!MD5:!SSLV2:!NULL
    SSLHonorCipherOrder on
    

The [SSLHonorCipherOrder directive](http://httpd.apache.org/docs/2.2/mod/mod_ssl.html#sslhonorcipherorder) is used to force the server's cipher choice on to the client.

And lets run the Cipher Suite string through `openssl ciphers` you can see the exact configurations that are being allowed:

    $ openssl ciphers 'RC4-SHA:AES128-SHA:ALL:!ADH:!EXP:!LOW:!MD5:!SSLV2:!NULL'
    
    RC4-SHA:AES128-SHA:DHE-RSA-SEED-SHA:DHE-DSS-SEED-SHA:SEED-SHA:
    DHE-RSA-AES256-SHA:DHE-DSS-AES256-SHA:AES256-SHA:DHE-RSA-AES128-SHA:
    DHE-DSS-AES128-SHA:EDH-RSA-DES-CBC3-SHA:EDH-DSS-DES-CBC3-SHA:DES-CBC3-SHA

This will use RC4, and fall back to AES-128, before going to other stronger ciphers, but over the defaults, it is significantly faster.



## SSL Session Cache and Resumption


mod_ssl's supports a plugable backend for storing client sessions with the [SSLSessionCache directive](http://httpd.apache.org/docs/2.2/mod/mod_ssl.html#sslsessioncache).  The two most commonly used are the _shm_ and _dbm_ on a single machine.  The shm backend is faster than dbm, and should be used in almost all cases.

However, as Adam noted, most people have more than one machine doing SSL Termination.  This means a distributed SSL session cache is needed.  I wrote the patch for mod_ssl to support a [memcached SSL Session cache 3 years ago](http://svn.apache.org/viewvc?revision=545379&view=revision).  This patch wasn't backported, so you'll need to use [Apache 2.3.x, which is currently in Alpha](http://httpd.apache.org/download.cgi#apache23).  To configure it, just pass a list of memcached nodes:

    SSLSessionCache memcache:10.0.0.1,10.0.0.2,10.0.0.3

## Reducing Round Trips


The best tool to measure this is [Wireshark](http://www.wireshark.org/), so you can see both the volume of data, and the round trips.  The easy way to test with this is using the `openssl s_client` command.  This command lets you easily create SSL connections, and tune various things on both the client and server.

Here is a truncated example of using s_client against encrypted.google.com:

    $ openssl s_client -debug -tls1 -host encrypted.google.com -port 443
    ..... data dumps .....
    ---
    SSL handshake has read 1893 bytes and written 285 bytes
    ---
    New, TLSv1/SSLv3, Cipher is RC4-SHA
    Server public key is 1024 bit
    Compression: NONE
    Expansion: NONE
    SSL-Session:
        Protocol  : TLSv1
        Cipher    : RC4-SHA
    ....

The interesting parts you can see here are both the negotiated ciphers, and the total bytes written by each side to establish the connection.  The majority of the data sent by the server is from the size of the server certificate.

As Adam discussed in depth, because [many certificates have a chain](http://en.wikipedia.org/wiki/Certification_path_validation_algorithm), and most are at least 2048 bits long, it is very easy for a new TCP connection to overflow your [initial TCP window](http://en.wikipedia.org/wiki/Slow-start).  Your goal is to make sure you are sending the correct chain, but not sending too much or irrelevant certificates.   Here is a example of www.cloudkick.com, which uses the GoDaddy CA, and an intermediate certificate:


    $ openssl s_client -tls1 -host www.cloudkick.com -port 443 -debug
    
    ---
    Certificate chain
     0 s:/O=*.cloudkick.com
          /OU=Domain Control Validated
          /CN=*.cloudkick.com
       i:/C=US
         /ST=Arizona
         /L=Scottsdale
         /O=GoDaddy.com, Inc.
         /OU=http://certificates.godaddy.com/repository
         /CN=Go Daddy Secure Certification Authority
         /serialNumber=07969287
     1 s:/C=US
           /ST=Arizona
           /L=Scottsdale
           /O=GoDaddy.com, Inc.
           /OU=http://certificates.godaddy.com/repository
           /CN=Go Daddy Secure Certification Authority
           /serialNumber=07969287
       i:/C=US
         /O=The Go Daddy Group, Inc.
         /OU=Go Daddy Class 2 Certification Authority
    ---
    ...............
    ---
    SSL handshake has read 2974 bytes and written 422 bytes
    ---
    ...............

In this case, the server sent the both the certificate for `*.cloudkick.com`, and the [Go Daddy intermediate certificate](https://certs.godaddy.com/anonymous/repository.seam).  Try as we might, the server in this case had to send 2974 bytes to get started, over 1000 bytes more than what encrypted.google.com needed.  This is just a reality of using a chain certificate, and using 2048 bit keys.   Just make sure you aren't sending extra certificates, and to keep your data bellow 4kb to prevent an ACK being needed in the small windows as TCP connections are being started.

## OCSP Stapling


One of the biggest problems with the existing SSL infrastructure is that validating the status of a certificate is hard and slow.   [OCSP Stapling](http://en.wikipedia.org/wiki/OCSP_Stapling) doesn't make it easier to understand, but it does at least make it faster.  OCSP stapling support was [originally funded from a grant by Mozilla](http://www.mozilla.org/grants/open-source-software-institute.html).  It has been added to Apache httpd 2.3, so you'll need to [download that alpha release](http://httpd.apache.org/download.cgi#apache23) in order to use it.

OCSP Stapling takes the Certificate's Authorities OCSP response and bundles it in the initial response to the client.  This OCSP response is a cryptographic signature verifying your certificate is still valid for X days. This means the client doesn't need to resolve another DNS name, and hit another service just to validate your certificate.

In Apache 2.3 and above, the configuration to enable OCSP Stapling is quite simple;  Just put these directives in your global scope:

    SSLUseStapling on
    SSLStaplingCache "shmcb:logs/stapling_cache(128000)"


You can test OCSP stapling using the `openssl s_client` command again and the -status parameter:

    $ openssl s_client -host encrypted.google.com -port 443 -tls1  -tlsextdebug  -status
    ....
    OCSP response: no response sent
    ....

Even Google hasn't enabled OCSP stapling yet!

If OCSP stapling was enabled, you would see something like this as the output:

    OCSP response: 
    ======================================
    OCSP Response Data:
        OCSP Response Status: successful (0x0)
        Response Type: Basic OCSP Response
        Version: 1 (0x0)
        Responder Id: C = US, ST = Arizona, L = Scottsdale, O = "GoDaddy.com, Inc.", 
                               OU = http://certs.godaddy.com/repository/, 
                               CN = Go Daddy Validation Authority
        Produced At: Jul 10 17:18:44 2010 GMT
        Responses:
        Certificate ID:
          Hash Algorithm: sha1
          Issuer Name Hash: 70292276537F1ABC8FD53C9484E914CB762A052A
          Issuer Key Hash: FDAC6132936C45D6E2EE855F9ABAE7769968CCE7
          Serial Number: 047C0A27B3C295
        Cert Status: good
        This Update: Jul 10 14:15:00 2010 GMT
        Next Update: Jul 10 23:18:44 2010 GMT


Here my server provided a signature from Go Daddy, saying that my certificate was valid for at least another 5 hours.


## False Start, Snap Start and Next Protocol Extensions


Google has proposed a series of extensions and modifications to the TLS protocol in order to reduce round trips, both at the initial negotiation, and when to start sending client data.

[TLS False Start](https://tools.ietf.org/html/draft-bmoeller-tls-falsestart-00) is mostly a client change, but even if you wanted to implement the proposed server false start, it really depends upon OpenSSL updates to support it.  The only recommendation here is to not use ancient versions of OpenSSL -- which is important anyways because of the [SSL Renegotiation attacks discovered last year](http://it.slashdot.org/story/09/11/16/2327230/slashdot.sourceforge.net).

The [Snap Start](http://tools.ietf.org/html/draft-agl-tls-snapstart-00) proposal will need server support, but currently no released version of OpenSSL supports it yet.

[Next Protocol Negotiation Extension](http://tools.ietf.org/html/draft-agl-tls-nextprotoneg-00) lets the client tell the server that it is gong to change protocols once the SSL negotiation finishes.  Conceptually to me this is similar to [Server Name Indication](http://en.wikipedia.org/wiki/Server_Name_Indication), where the client is leaking application logic to the SSL layer.   This will make upgrades to the [SPDY protocol ](http://www.chromium.org/spdy/spdy-protocol)faster, but again there is not a released version of OpenSSL with support yet.



## The missing patches

* Adam mentions a patch reducing OpenSSL's default buffer allocations from 50kb to 5kb, and suggests the Tor project has a similar patch.  I have been unable to find it.
* I was unable to find any patches for the Next Protocol Negotiation Extension.


## Closing



Hopefully your `mod_ssl` site is faster after all of this, but if you have any recommendations or ideas to improve it further, please let me know!

