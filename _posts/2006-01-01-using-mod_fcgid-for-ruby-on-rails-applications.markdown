---
date: '2006-01-01 16:22:13'
layout: post
slug: using-mod_fcgid-for-ruby-on-rails-applications
status: publish
title: Using mod_fcgid for Ruby on Rails Applications
wordpress_id: '120'
---


Many people know about the old school [mod_fastcgi](http://www.fastcgi.com/), but very few know about [mod_fcgid](http://fastcgi.coremail.cn/). To put it extremely briefly, if you are using Apache 2, and you should be, you should be using mod_fcgid, and not mod_fastcgi.



Here quick guide on how to configure mod_fcgid for use with Apache HTTPD 2.2.0 and [Typo](http://typo.leetsoft.com/trac/), a RoR blog engine:

* Download and Prepare mod_fcgid

>    wget http://fastcgi.coremail.cn/mod_fcgid.1.07.tar.gz
>    tar -xvzf mod_fcgid.1.07.tar.gz
>    cd mod_fcgid.1.07

* Edit the Makefile.  Change the `_top_dir` variable to the prefix of your Apache 2 install.


* Apply [this patch for mod_fcgid](http://constant.northnitch.com/~chip/mod_fcgid.1.07-apache2.2.0.patch):


>     wget http://constant.northnitch.com/~chip/mod_fcgid.1.07-apache2.2.0.patch
>     patch -p0 < mod_fcgid.1.07-apache2.2.0.patch



This patch has been submitted upstream, and should be part of the next release.


* Run 'make'.


* Copy _.libs/mod_fcgid.so_ to your Apache modules directory


* Add the following to your httpd.conf, to load the module:


>
>     LoadModule fcgid_module modules/mod_fcgid.so 
>     IPCCommTimeout 40
>     IPCConnectTimeout 10
>     
> 
> 






* Configure mod_fcgid for your Rails Application:

> 
>     
>     
>     <VirtualHost *:80>
>     ...
>     # Insert the rest of your vhost config here.
>     ServerName foo.example.com
>     
>     <Location /journal>
>         RewriteEngine On
>         # Let apache handle purely static files like images by itself.
>         RewriteCond %{REQUEST_FILENAME} !-f
>         # Send Everything else to Typo
>         RewriteRule ^(.*)$ dispatch.fcgi [QSA,L] 
>     </Location>
>     
>     <Directory /sites/foo.example.com/public_html/journal>
>         # ExecCGI is required for mod_fcgid to work.
>         Options Indexes FollowSymLinks ExecCGI
>         # Disable .htaccess files.
>         AllowOverride None
>         Order allow,deny
>         Allow from all
>         # This tells mod_fcgid to run the dispatch.fcgi script as a FastCGI
>         AddHandler fcgid-script .fcgi
>     </Directory>
>     ....
>     </VirtualHost>
>     
> 






* Thats it.





This whole process can be easier, since mod_fcgid is also in many packaging systems, including [FreeBSD's Ports](http://www.freshports.org/www/mod_fcgid), and [Gentoo Portage](http://packages.gentoo.org/packages/?category=www-apache;name=mod_fcgid).

