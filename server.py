import logging
import datetime
import sys
import socket as so
from threading import Thread
from config import read_entry

PATH = sys.path[0]
LOGPATH = PATH + '/serverlogs'

SERVERPORT = int(read_entry('mainserverport', 'Global'))
RESPONSEPORT = int(read_entry('responseport', 'Global'))

timestr = datetime.datetime.now().strftime('%d-%m-%y==%H-%M-%S')
f = open(LOGPATH + '/server' + timestr + '.log', 'w')
f.close()
logging.basicConfig(filename=LOGPATH + '/server' + timestr + '.log', level=logging.DEBUG)


def log(msg):
    logging.debug(msg)
    print(msg)


class _Server:
    """class for all server commands"""
    stop = False

    def _send_back_to_client(addr, msg: str):
        sock = so.socket(so.AF_INET, so.SOCK_STREAM)
        sock.connect((addr, RESPONSEPORT))
        sock.send(msg.encode('utf-8'))
        sock.close()


class RecvConnection(Thread, _Server):

    def __init__(self):
        super().__init__()
    def run(self):
        sock1 = so.socket()
        sock1.bind(('', SERVERPORT))
        log('binded listen socket at 1337')
        while True:
            if _Server.stop:
                break
            log('sock is listening')
            sock1.listen(5)
            conn, addr = sock1.accept()
            thread = HandleConnection(conn, addr)
            thread.start()




class HandleConnection(Thread):
    def __init__(self, conn: so.socket, addr):
        super(HandleConnection, self).__init__()
        self.ipaddr = addr[0]
        self.conn = conn
        log(str(self.conn))

    def run(self):
        msg = self.conn.recv(8192).decode('utf-8')
        header = msg.split('><')[0]
        log(msg)
        self.conn.close()


if __name__ == '__main__':
    t = RecvConnection()
    t.start()
    while True:
        i = input()
        if i == 'stop':
            _Server.stop = True
            sys.exit(0)
