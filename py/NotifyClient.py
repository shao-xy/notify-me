import socket

from commondefs import WEBSERVER_LISTEN_PORT

class NotifyClient():
  def __init__(self):
    self._s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  def send(self, title, body):
    try:
      self._s.connect((socket.gethostname(), WEBSERVER_LISTEN_PORT))
      self._s.send((title + '\n' + body).encode('utf-8'))
      self._s.close()
    except ConnectionRefusedError:
      return -1
    return 0
