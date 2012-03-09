---
date: '2008-12-23 18:33:56'
layout: post
slug: mod_lua-in-apache-trunk
status: publish
title: mod_lua in apache trunk
wordpress_id: '254'
---

The module formally known as [mod_wombat](http://www.google.com/search?q=mod_wombat) was renamed [mod_lua](https://svn.apache.org/repos/asf/httpd/httpd/trunk/modules/lua/), and has pulled into the Apache HTTP Server trunk, and will be part of the future 2.4 stable release.

For an example of why it is cool, lets look at replacing a common task with mod_rewrite: Blocking Image Theft.

The HTTPD wiki even [has an example of how to do](http://wiki.apache.org/httpd/RewriteImageTheft) this for us:


    RewriteEngine on
    RewriteCond %{HTTP_REFERER} !=""
    RewriteCond %{HTTP_REFERER} !example\.com [NC]
    RewriteRule \.(jpe?g|gif|png)$ - [F,NC]`


With the new mod_lua, you can do this using real if statements and functions.

For example:


    <LuaHookTranslateName imagetheft>
    function is_image(path)
       -- You could put complicated regular expressions here.
       if path:match("%a+.png") then
           return true
       end
       return false
    end

    function imagetheft(r)
       if not is_image(r.uri) then
           return apache2.DECLINED
       end

       referer = r:headers_in("Referer")
       if referer then
           if referer:find('example.com') then
               return apache2.DECLINED
           else
               r:err("Forbidden for Image Theft! uri=".. r.uri)
               return 403
           end
       end
       return apache2.DECLINED
    end
    </LuaHookTranslateName>




While this example comes out signifigantly longer, I do believe in the long run it will let people write more maintainable configurations, espcially for things like complicated RewriteRules -- since basic things that have long be obsecured into [RewriteCond](http://httpd.apache.org/docs/trunk/mod/mod_rewrite.html#rewritecond) can now be easily accessed and evaluated with an If statement in [Lua](http://www.lua.org/).

Much of the API is still in flux, but hopefully we will come up with some shortcut builtins that make many common taskes easier and shorter.
