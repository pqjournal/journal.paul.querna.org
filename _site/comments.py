#!/usr/bin/python

import cgi, cgitb

cgitb.enable(display=True, logdir="/tmp")

import sys
import subprocess

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


def handle_comment():
    form = cgi.FieldStorage()
    targetpost = form.getfirst("targetpost", None)
    name = form.getfirst("name", None)
    link = form.getfirst("link", None)
    comment = form.getfirst("comment", None)

    if not targetpost:
        r = ErrorResponse("targetpost is a required field.")
        r.send()
        return

    if not name:
        r = ErrorResponse("name is a required field.")
        r.send()
        return

    if not comment:
        r = ErrorResponse("comment is a required field.")
        r.send()
        return

    lock = FileLock("/some/file/or/other")
    with lock:
        print lock.path, 'is locked.'

if __name__ == "__main__":
    conf = get_config()
    if not conf:
        r = ErrorResponse("Comments system is misconfigured.")
        r.send()
    else:
        handle_comment()
    sys.exit(0)
