from django.apps import AppConfig

import socket
import threading
from . import views
import os


def tcp_server(ip, port):
    print('start tcp server')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((ip, port))
    s.listen(1)
    while True:
        conn, addr = s.accept()

        print('connected:', addr)

        while True:
            data = conn.recv(1024)
            if not data:
                break
            views.process_message(data.decode())

        conn.close()


class AppConfig(AppConfig):
    name = 'app'

    def ready(self):
        if os.environ.get('RUN_MAIN', None) != 'true':
            t = threading.Thread(target=tcp_server, args=('localhost', 9090))
            t.daemon = True
            t.start()
