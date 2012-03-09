---
date: '2004-12-01 01:15:00'
layout: post
slug: mod_svn_view-development
status: publish
title: mod_svn_view development
wordpress_id: '45'
---

Added two big features to [mod_svn_view](http://www.outoforder.cc/projects/apache/mod_svn_view/) recently:  
  

**[mod_authz_svn](http://svnbook.red-bean.com/en/1.1/ch06s04.html#svn-ch-6-sect-4.4.2) support!** `mod_svn_view` can now use the same Path Based Authorization files as many mod_dav_svn users use.



    SVNViewAuthzSvnFile /test/trunk/svn-authz



This eliminates the need to duplicate access control. You can se one file to control both mod_dav_svn users, and all access from mod_svn_view.  I don't believe any of the alternatives like [WebSVN](http://websvn.tigris.org/), [ViewCVS](http://viewcvs.sourceforge.net/) or [Chora](http://www.horde.org/chora/) support this.
  
  

**New Themes System.**  I want to make it extremely easy for end users to customize mod_svn_view, so now its even easier to create and manage themes.
Here is the new filesystem layout:

    
    
    themes/
        blueview/
            style.css
            images/
                file.png
                dir.png
                parent.png
    


This is Configured in Apache using two Directives:



    SVNViewThemesDir /test/sv/themes
    SVNViewTheme blueview

# We must also allow file system access to the themes directory:  

    <Directory "/test/sv/themes">
        Order allow,deny
        Allow from All
        Deny From none
    </Directory>


`mod_svn_view` will translate any svn-view urls that start with _/*theme*/_ to the active theme directory.  For example,
a request for '/svn-view/*theme*/style.css' will be translated to '/test/sv/themes/**blueview**/style.css'.  
  
This allows one XSL file to be used for every CSS or image based theme.  This eliminates the need for administrators to copy the CSS or image files into their DocumentRoot, as mod_svn_view handles all of the URL translation itself.
  
  

I am starting to get very happy with mod_svn_view.  There are now only 3 things left on my list to fix before an initial public offering:


  * Cleanup of Time/Date Display.  I am not sure if I want to use the '20 Days Ago' type string that ViewCVS has made common, or a more traditional 'MM/DD/YYYY HH:MM' format.  The current one looks like _'2004-03-18T18:37:48.276683Z'_.  This is a show stopper for a public release.

  * Finish Blame Support.  I am about 50% done writing my Server Side Blame code.  As with the Authz support, the other alternatives do not support this.

  * Pretty Icons.  I am still looking for a good set of Icons that I can include in an initial release of mod_svn_view.  I want the default/first theme to be really good.  Just look at how many ViewCVS installations use the default theme.  I want mine to look nice, and have the best features compared to any Web Based Viewer of Subversion Repos.



I will try to get up a demo server later this week so the world can examine the progress.


_Edit:_ Trying to fix the formating of a >code< block insdie a >list<.  Stupid BBCode.  

_Edit #2:_ Explain the file translation stuff better.
