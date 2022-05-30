#!/usr/bin/env python3

COMMON_HTML_HEADER = 'Content-type: text/html\n\n'
COMMON_RESPONSE = """
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>OK!</title>
</head>
<body>
</body>
</html>
"""
import sys
import os

import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
print(COMMON_HTML_HEADER)
sys.stdout.flush()

import cgi
import cgitb
cgitb.enable(display=1, logdir=os.path.join(os.path.dirname(sys.argv[0]), 'log'))

sys.path.insert(0, '/home/daniel/coding/cgi/notify/py')
from NotifyClient import NotifyClient

#os.environ['LOGNAME'] = 'daniel'
#os.environ['HOME'] = '/home/daniel'
#os.environ['USER'] = 'daniel'
#os.environ['XDG_RUNTIME_DIR'] = '/run/user/1000'
#os.environ['DBUS_SESSION_BUS_ADDRESS'] = 'unix:path=/run/user/1000/bus'
#import notify2

def parse_args():
  cookies = None
  if 'HTTP_COOKIE' in os.environ:
      cookie_string = os.environ.get('HTTP_COOKIE')
      c = Cookie.SimpleCookie()
      c.load(cookie_string)
      cookies = { k: c[k].value for k in c.keys() }

  cgi_storage = cgi.FieldStorage()
  cgidata = { k: cgi_storage.getvalue(k) for k in cgi_storage.keys() }

  remote_addr = 'REMOTE_ADDR' in os.environ and os.environ['REMOTE_ADDR'] or ''
  return cookies, cgidata, remote_addr

def main():
  cookies, cgidata, remote_addr = parse_args()
  title = 't' in cgidata and cgidata['t'] or '(no title)'
  body = 'b' in cgidata and cgidata['b'] or '(no body)'

  NotifyClient().send(title, body)
  print(COMMON_RESPONSE)

  return 0

if __name__ == '__main__':
  sys.exit(main())
