from config import read_entry
import socket
import logging as log
from threading import Thread


class Connect:
    @staticmethod
    def _connect(header: str, msg: str) -> str:
        msg = header + '><' + msg
        log.debug('Connection to server with message: ' + msg)
        s1 = socket.socket()
        s1.connect(((read_entry("serverip")), int(read_entry("serverport"))))
        s1.send(msg.encode('utf-8'))
        s1.close()
        s2 = socket.socket()
        s2.bind(((read_entry("serverip")), int(read_entry("responseport"))))
        s2.listen(1)
        conn, _ = s2.accept()
        return conn.recv(8192).decode('utf-8')

    @staticmethod
    def get_fixture(league):
        return Connect._connect('FIXTURE', league)


class __Test:

    def __init__(self):
        s = socket.socket()
        s.connect(('localhost', 5938))


if __name__ == '__main__':
    __Test()
