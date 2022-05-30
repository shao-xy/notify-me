import sys
import socket
from threading import Thread

from commondefs import WEBSERVER_LISTEN_PORT

import Notifier

class ServingThread(Thread):
    def __init__(self, clientsockettuple):
        Thread.__init__(self)
        self.clientsocket, self.addr = clientsockettuple

    def run(self):
        msg = self.clientsocket.recv(4096).decode('utf-8').strip()
        delim = msg.find('\n')
        if delim == -1:
          title = 'Remote message'
          body = msg
        else:
          title = msg[:delim]
          body = msg[delim + 1:]
        print(f'[REQ] {self.addr}: {title} | {body}')
        Notifier.notify(title, body)

class Server(Thread):
    def __init__(self, tracer_daemon):
        Thread.__init__(self)
        self._daemon = tracer_daemon
        self._thrdpool = []

    def run(self):
        print('Server thread launch!')
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.bind((socket.gethostname(), WEBSERVER_LISTEN_PORT))
        serversocket.listen(5)
        while True:
            new_thrd = ServingThread(serversocket.accept())
            new_thrd.start()
            self._thrdpool.append(new_thrd)
    
    def __del__(self):
        for thrd in self._thrdpool:
            thrd.join()
