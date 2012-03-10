#!/usr/bin/python

import cgi, cgitb

cgitb.enable(display=True, logdir="/tmp")

import sys
import os
from os.path import join as pjoin
import subprocess
import tempfile
import shutil
import yaml
import time
import re


class Response(object):
    def __init__(self, output = None):
        if output == None:
            output = sys.stdout
        self.output = output
        self.headers = ["Content-Type: text/html",]
        self.body = ""

    def send(self):
        for header in self.headers:
            self.output.write(header + "\n")
        # end headers
        self.output.write("\n")
        self.output.write(self.body)

class ErrorResponse(Response):
    def __init__(self, msg = None, output = None):
        super(ErrorResponse, self).__init__(output)
        self.msg = msg
        self.headers.append("Status: 400")

    def send(self):
        self.body = "<h2>Error</h2>\n"
        self.body += "<div>%s</div>\n" % (cgi.escape(self.msg))
        super(ErrorResponse, self).send()

def get_config():
    conf = {}
    conf['git_root'] = os.environ.get('COMMENTS_GIT_ROOT')

    if not conf['git_root']:
        return False

    return conf

def slugify(value):
    """
    Taken directly from Django.

    Normalizes string, converts to lowercase, removes non-alpha characters,
    and converts spaces to hyphens.
    """
    import unicodedata
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
    value = unicode(re.sub('[^\w\s-]', '', value).strip().lower())
    return str(re.sub('[-\s]+', '-', value))

def rand_hash(max_length):
    val = os.urandom((max_length + 1) / 2).encode('hex').lower()
    val = val[:max_length]
    return val

def git_clone(origin):
    subprocess.check_output(['/usr/bin/git', 'clone', origin, 'wc'], stderr=subprocess.STDOUT)

def check_post_exists(base, target):
    post = pjoin(base, '_posts', target + ".markdown")
    if not os.path.exists(post):
        r = ErrorResponse("Invalid target blog post")
        r.send()
        return False
    return True

def validate(targetpost, name, comment):
    if not targetpost:
        r = ErrorResponse("targetpost is a required field.")
        r.send()
        return False

    if not name:
        r = ErrorResponse("name is a required field.")
        r.send()
        return False

    if not comment:
        r = ErrorResponse("comment is a required field.")
        r.send()
        return False
    return True

def handle_comment(conf):
    form = cgi.FieldStorage()
    targetpost = form.getfirst("targetpost", '2012-03-01-march-2012')
    name = form.getfirst("name", None)
    website = form.getfirst("website", None)
    email = form.getfirst("email", None)
    comment = form.getfirst("comment", None)

    #if not validate(targetpost, name, comment):
    #    return

    tmppath = tempfile.mkdtemp(prefix='tmp-git-comments')
    curpath = os.getcwd()

    try:
        os.chdir(tmppath)
        git_clone(conf['git_root'])
        os.chdir('wc')
        target = os.path.basename(targetpost)
        base = pjoin(tmppath, 'wc')

        if not check_post_exists(base, target):
            return

        cdir = pjoin(base, '_comments', target)
        if not os.path.exists(cdir):
            try:
                os.mkdir(cdir)
            except:
                pass

        datestr = slugify(unicode(time.strftime('%Y-%m-%d_%H:%M')))
        ipstr = slugify(unicode(os.environ['REMOTE_ADDR']))
        rstr = rand_hash(8)

        cpath = pjoin(base, '_comments', target, "%s-%s-%s.yml" % (datestr, ipstr, rstr))
        doc = {
            'ip_address': os.environ['REMOTE_ADDR'],
            'name': name,
            'website': website,
            'email': email,
            'comment': comment,
        }

        with open(cpath, 'w') as fp:
            yaml.safe_dump(doc, fp)

        r = Response()
        r.body = open(cpath).read()
        r.send()
    finally:
        #shutil.rmtree(tmppath, ignore_errors=True)
        os.chdir(curpath)


if __name__ == "__main__":
    conf = get_config()
    if not conf:
        r = ErrorResponse("Comments system is misconfigured.")
        r.send()
    else:
        handle_comment(conf)
    sys.exit(0)
