#!/usr/bin/env python3

import sys
import os
import cgi
import cgitb
cgitb.enable(display=1, logdir='./log')

import notify2

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

  notify2.init(title)
  notify2.Notification(str(title), str(body)).show()

  return 0

if __name__ == '__main__':
  sys.exit(main())
