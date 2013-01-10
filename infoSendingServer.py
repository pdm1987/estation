# -*- coding: gbk -*-
'''
���չ涨��ʽ��վ�Ʒ�����Ϣ,����Ϣ���,������վid����Ϣ�����͵���Ӧ��TCP����
'''
import threading.Thread
import socket
import network

class handleSending(threading.Thread):
    def __init__(self, conn, addr, pool):
        self.pool=pool
        self.conn=conn
        self.addr=addr
    
    def run(self):
        
        return


class infoSendingServer(threading.Thread):
    def __init__(self, pool):
        threading.Thread.__init__(self)
        self.pool=pool
        self.running=True
    
    def run(self):
        sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((network.HOST, network.PORT_OF_NETCONFIG))
        sock.listen(1)
        while self.running:
            conn, addr=sock.accept()
            new_t=handleSending(conn, addr, self.pool)
            new_t.start()
        return
    
    def stop(self):
        self.running=False
        print('exit infoSendingServer')



if __name__=='__main__':
    print('test infoSendingServer')
