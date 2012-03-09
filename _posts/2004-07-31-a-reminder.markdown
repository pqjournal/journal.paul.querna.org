---
date: '2004-07-31 04:27:57'
layout: post
slug: a-reminder
status: publish
title: A reminder....
wordpress_id: '29'
---

Here is a reminder why <a href="http://www.boost.org/libs/python/doc/" class="ng_url">Boost::Python</a> and C++ Templates in general are evil:

Quote from gcc error message:

<blockquote>
In function `boost::python::api::object boost::python::detail::make_function_aux&lt;void (pyPythonMsg::*)(int), boost::python::default_call_policies, boost::python::detail::args_from_python, boost::mpl::list3&lt;void, pyPythonMsg&amp;, int&gt;, boost::mpl::int_&lt;0&gt; &gt;(void (pyPythonMsg::*)(int), boost::python::default_call_policies const&amp;, boost::python::detail::args_from_python const&amp;, boost::mpl::list3&lt;void, pyPythonMsg&amp;, int&gt; const&amp;, std::pair&lt;boost::python::detail::keyword const*, boost::python::detail::keyword const*&gt; const&amp;, boost::mpl::int_&lt;0&gt;)':
</blockquote>
