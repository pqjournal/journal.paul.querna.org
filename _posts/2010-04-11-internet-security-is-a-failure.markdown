---
date: '2010-04-11 18:26:22'
layout: post
slug: internet-security-is-a-failure
status: publish
title: Internet Security is a failure
wordpress_id: '341'
---

Security on the Internet sucks, and it is only getting worse.  The problem is systemic, with security researchers and developers not producing viable ways for the average user to live on the Internet in a secure fashion without excessive paranoia.

**The story of Apache's Infrastructure**

The [Apache Software Foundation](http://www.apache.org/) runs [about 40 machines](http://monitoring.apache.org/status/), with varying access policies, but some have upwards of 2300 shell accounts, one for every commiter.  In the last year, there have been three major incidents in this infrastructure:



	
  * The first attack was in August 2009 was caused by misconfiguration of our backup procedures, and is detailed in[ this downtime report](https://blogs.apache.org/infra/entry/apache_org_downtime_report).

	
  * The second attack was a persistent DDoS attack against [issues.apache.org in October 2009](https://blogs.apache.org/infra/entry/ddos_mystery_involving_linux_and).

	
  * The third attack started this week, was a directed attack against the Apache JIRA instance, targeting individual Apache Infrastructure team members.  Full details have not yet been posted online about this attack, but you can see [the initial email from Joe](http://people.apache.org/~joes/jira-hacked.txt) [gpg signature](http://people.apache.org/~joes/jira-hacked.txt.asc).  Hopefully later this week, we will get up a blog post with full details.


As a mostly volunteer organization, it is difficult to implement draconian security policies, but the ASF  has avoided running most dynamic webapps -- the vast majority of our websites are static HTML.  Maybe this has saved us from untold other security issues, but even with our believed limited exposure, we still got hacked.

The ASF is by no means perfect, it has half-implemented some of the best practices we know we need to do, but I believe overall the ASF is more secure than most big companies.  It has some of the best sysadmins I have known, but it still has issues.   Maybe we can just blame that on having too many users, but I believe fundamentally, Internet security is a failure.

I believe there are four major facets around our insecure Internet:

	
  1. Identity and Authentication

	
  2. Transport Security

	
  3. Secure Software and Operating Systems

	
  4. Law Enforcement


**Identity and Authentication: Failed.**

If there was one thing I would change, it would be to stop everyone in the world from using **Passwords**.  Individuals might pick good ones, but on a whole, they pick bad passwords.  They also use the same password across a multitude of services.

The problem is most attackers collect these passwords, and then use them to escalate privileges to more services.

Wait a minute you might ask, you just combined Identity with  Authentication, but they are different!  And yes, you are right, but for  the common user, they don't know the difference.  To solve both on a wide scale, I believe their issues are joined at the hip, as authentication depends on identity in most important use cases.

There are many ways you can avoid using passwords, but they are all too difficult for the average user and widespread adoption.

[OpenID](http://openid.net/) was one of the first real innovators in this area, and much credit is due to [Brad](http://www.bradfitz.com/) for it. Even though [most people on the internet likely have a provider](http://openid.net/get-an-openid), very few use it on a daily basis.  Between the user experience issues and [phishing problems,](http://wiki.openid.net/OpenID_Phishing_Brainstorm) I do not believe OpenID will ever be a real replacement for passwords for all websites.  It has solved many problems like how to comment on a blog -- which is great, I hate blog spam -- but it isn't the end of Identity and Authentication.

[OAuth](http://oauth.net/) is taking a different approach, and solving a different problem, which is great for my twitter account.  It is still too early to know if OAuth will really improve the wide-scale security of connected web services, but it has been three years since the project started and real-world use cases are still limited.  The standard [still changing quickly](http://wiki.oauth.net/OAuth-WRAP) certainly isn't helping adoption.

Both Amazon Web Services and PayPal let you [use multi-factor authentication](http://en.wikipedia.org/wiki/Two-factor_authentication) easily, and I applaud them for this, but most websites and services do not, notability for things like email, which today is the primary identify of most people on the Internet.  I believe more services should adopt SMS based multi-factor authentication, and products like [Twilio's SMS](http://www.twilio.com/sms/) API make this easier than ever.  I still can count on a single hand the services I have ever logged into using MFA though -- I still can't login to [my bank](https://www.wellsfargo.com/) with it, nor my email. Companies like [YubiCo](http://yubico.com) are also providing open stacks to improve security, but again most people don't own a token.

You can find limited cases of SSL Client Certificates being useful and working, but on the whole they are still painful with many sharp edges.  I used client certificates [extensively at Joost](http://journal.paul.querna.org/articles/2009/07/29/leaving-joost/), and I never ever want to repeat that experience, and I am a fairly technical user.   The difficulties are not just on the clients and users, but also on running a Certificate Authority correctly with the right policies, revocations and security models.

It isn't just the users that have problems -- providers like DreamHost are unable to authenticate their own users, [letting attackers take over accounts mostly via social engineering](http://news.ycombinator.com/item?id=1229247).

**Transport Security: Failed.**

As part of the [TLS protocol,](http://en.wikipedia.org/wiki/Transport_Layer_Security) you need to establish trust between various parties, and so for the most common configurations on the Internet, SSL/TLS depends upon [Certificate Authorities](http://en.wikipedia.org/wiki/Certificate_authority).

Trusting Certificate Authorities has turned into an oxymoron.  With Certificates being shipped that [no one even knows how they got in the trusted list,](http://news.ycombinator.com/item?id=1244444) to the threat of [man in the middle attacks from valid certificates](http://news.ycombinator.com/item?id=1234460), to [off the shelf devices for sale to attack it](http://arstechnica.com/security/news/2010/03/govts-certificate-authorities-conspire-to-spy-on-ssl-users.ars), TLS has failed.

In addition the problems of [the SSL renegotiation attacks](http://it.slashdot.org/story/09/11/16/2327230/SSL-Renegotiation-Attack-Becomes-Real) don't help the situation, and it will take years before everyone has [upgraded their SSL software to](http://www.openssl.org/news/secadv_20091111.txt) prevent this exploit.

I believe while issues in the TLS protocol itself are going to be rare overall, the problem of the CAs will not go away.  I don't know how to solve the trusted CA problem -- distributed trust systems are one of the hardest problems to solve for the average end user.  As a normal user, at some point you will need to trust a large company to make trust decisions for you, but this process is still too opaque to provide real trust for most people.  I personally have doubts that the [Extended Validation Certificates](http://en.wikipedia.org/wiki/Extended_Validation_Certificate) are a good thing, in fact I believe it might be providing an illusion of being more secure. We are still trusting the same Certificate Authorities that have almost zero business motivation to provide good security.

**Secure Software and Operating Systems: Failed.**

Do your Linux servers have an uptime of over 30 days?  Then it is very likely they have a [local root kernel exploit](http://www.ubuntu.com/usn/USN-914-1).  It used to be funny to make fun of Windows exploits, and there have been many remote ones which is terrible, but Linux and most open source alternatives have not truly improved security for the average server.  The problem isn't just that the operating system kernels are insecure, it is that privilege escalation is far too easy, and far too common.

You should design software around expecting a local user to be compromised, and not to pick on projects like Wordpress, but they have seen a rash of severe security issues over the years, with a relatively small code base -- and most webapps, open source or not have similar records.   The problem is once an attacker can execute local code, in almost all situations it means with a little work, they can also gain root.

On the user's side, browsers and their plugins, [like flash](http://www.f-secure.com/vulnerabilities/SA200900917),  have had a similarly abysmal track record.  Real innovation has come from Google Chrome, and most other browsers [are copying these methods](https://wiki.mozilla.org/Electrolysis). This is a very good thing. Hopefully it will reduce the size of [botnets](http://en.wikipedia.org/wiki/Botnet) in the future, but today most users are vulnerable to a multitude of remote attacks.

**Law Enforcement: Failed.**

In most cities, crime isn't a major problem anymore.  You still lock your doors, take basic [precautions with your bike](http://www.kryptonitelock.com), but the truth is, if someone really wanted to steal something from you, they probably could, but crime is not rampant.  You have an expectation that law enforcement will help you.

While law enforcement can sometimes turn a blind eye to a class of crimes, often [victimless ones](http://en.wikipedia.org/wiki/Victimless_crime), they have on the whole turned a blind eye to Internet hacking.  As long as [an attacker doesn't go after Sarah Pallin's email](http://en.wikipedia.org/wiki/Sarah_Palin_email_hack), there are rarely any consequences for most incidents.

Inside Apache, we have discussed [going to the FBI](http://www.fbi.gov/cyberinvest/cyberhome.htm) several times, but the conclusion every time is it would be a waste of our time.  The FBI doesn't care about our problems, because we aren't a political candidate, nor do we have millions of credit cards.    They have their [Internet Crime Complaint Center (IC3),](http://www.ic3.gov/default.aspx) but I believe its just a synonym for '[circular file](http://www.urbandictionary.com/define.php?term=circular%20file)'.

Obama's White House  has published their [Cyberspace Policy Review (PDF)](http://www.whitehouse.gov/assets/documents/Cyberspace_Policy_Review_final.pdf), and it talks about many great points, but it does not actually bring change to the Internet in any measurable fashion.

I don't want to [lock up 12 year old kids for the rest of their lives](http://www.itsecurity.com/features/hacker-high-061008/) because they defaced some website, but there must be a better framework and structure for prosecuting attackers world wide.  No matter the  improvements made to software, users, or best practices, with attackers essentially taking zero risk of ever getting caught today, they have no motivation to stop.

**What now?**

People are working on making the Internet a better place, but it isn't enough.  Everyone, in every part of the stack must care about their security.  Providers, both big and small, software developers, open source and proprietary, users both advanced and novice, they all live in a difficult world, and most of them live in an insecure one.

We won't all switch to [OpenBSD](http://www.openbsd.org/security.html).  We won't all switch to [Chrome](http://blog.chromium.org/2008/10/new-approach-to-browser-security-google.html).   We won't all stop [using passwords](http://www.yubico.com/products/yubikey/).  And [the government can't save you either](http://www.us-cert.gov/cas/tips/).

I wish I had a single answer, I dream that it was a solvable problem.  **As a technical person, I am more scared of having my own identity stolen, than of any terrorists attacks.**

Right now, the mission is on the individual to make smart choices, and do their best, but the only way the world will truly be a better place is if there is a systemic shift, to caring about security of the average human on the Internet, and maybe it will be big companies like Google or Microsoft that end up conquering this problem, but I hope we can learn form existing open source patterns, and find a better distributed way.

