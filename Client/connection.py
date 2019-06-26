from config import read_entry
import socket
import logging as log
import json
from threading import Thread


class Connect:
    @staticmethod
    def _connect(header: str, msg: str):
        msg = header + '><' + msg
        log.debug('Connection to server with message: ' + msg)
        s1 = socket.socket()
        s1.connect(((read_entry("serverip", 'Global')), int(read_entry("mainserverport", 'Global'))))
        s1.send(msg.encode('utf-8'))
        s1.close()
        s2 = socket.socket()
        s2.bind(((read_entry("serverip", 'Global')), int(read_entry("responseport",  'Global'))))
        s2.listen(1)
        conn, _ = s2.accept()
        recv = conn.recv(8192).decode('utf-8')
        ls = ['FIXTURE']
        st = []
        if header in ls:
            return json.loads(recv)

    @staticmethod
    def get_fixture(league):
        return type(Connect._connect('FIXTURE', league))



class __Test:

    def __init__(self):
        print(Connect.get_fixture('Premier League'))


if __name__ == '__main__':
    __Test()
