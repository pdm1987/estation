# -*- coding: gbk -*-
'''
busStopServer ���÷���
busStopServer.py ����busStop Info,����busStop Info���浽busStopTable��.
busStopTable�Ķ����table_busStop.py
'''

import socket
import network
import _thread
from table_busStop import busStopInfo

RUNNING=True

def busStopServerInput():
    global RUNNING
    
    while True:
        s=input()
        if s=='q':
            RUNNING=False
            break
    exit()
    return


def busStopServer(t_stop):
    global RUNNING
    _thread.start_new_thread(busStopServerInput, ())
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((network.HOST, network.PORT_OF_BUSSTOP))
    s.listen(1)
    while RUNNING:
        conn, addr=s.accept()
        print('Connected by',  addr)
        data=conn.recv(1024)
        if data:
            print(data)
            sdata=data.decode('utf8')
            print(sdata)
            arr=sdata.split()
            info=busStopInfo(arr[0], int(arr[1])) #ֱ�ӽ�lines��Ϊ��������������������,ʹ��setLines
            info.setLines(arr[2:])
            t_stop.add(info)
            #����ʱ��tableд�뵽�ļ���,�ǲ���ʱע�͵�
            t_stop.writToFile()
            conn.sendall(network.NET_RET_OK)
        print(RUNNING)
        conn.close()
    return


if __name__=='__main__':
    from table_busStop import table_busStop
    def test():
        
        print('test')
        t_stop=table_busStop()
        busStopServer(t_stop)
        return
    
    test()
