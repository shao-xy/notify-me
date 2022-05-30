#!/usr/bin/env python3

XDG_RUNNER_UID = 1000
XDG_RUNNER_GID = 1000

import sys
import os
from webserver import Server

class NotifyServer:
  def __init__(self):
    self.server = Server(self)

  def launch(self):
    self.server.start()

def check_uid():
  if os.getuid() != 0:
    sys.stdout.write('Must be root to execute.\n')
    sys.exit(-1)

def set_uid():
  with open('/var/run/temperature_pid', 'w') as fout:
    fout.write(str(os.getpid()))
  os.setgid(XDG_RUNNER_GID)
  os.setuid(XDG_RUNNER_UID)

def main():
  #check_uid()
  #set_uid()
  NotifyServer().launch()

if __name__ == '__main__':
  sys.exit(main())
