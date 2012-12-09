# -*- coding: gbk -*-
'''
busDataServer.py ���չ�����˾�Ĺ�����GPS����.
����ӿ���Ҫ�Թ����������Ĺ���,���㽫���ݷ��͹���.

busDataServer.py ������һֱ��ȡ����˿ڴ���������.
��������
    1.д�뵽�ļ���
    2.���ú�̨���������
    
busDataServer.py ����ֱ������վ�����س���֪ͨ��رջ�ϵͳ����.
�������� busDataServer �ĳ����� busDataServer �رպ���쳣���Բ��ٴη�����������.

'''

import socket
import network
import atexit

FILENAME='busData.txt'
file=None


def exit_server():
    global file
    file.close()
    return


def write_to_file(data):
    file.write(data)
    return


funclist=[write_to_file]

'''
����:
    flag:0 д���ļ� 1.���ú���
'''
def busDataServer(flag):
    global file
    running=True
    
    dofunc=funclist[flag]
    
    try:
        file=open(FILENAME, 'a')
    except IOError:
        print('open file error')
    else:
        print('open file ok')
        atexit.register(exit_server)
    
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((network.HOST_OF_BUSDATA, network.PORT_OF_BUSDATA))
    sock.listen(1)
    while running:
        conn, addr=sock.accept()
        print('Connected by ',  addr)
        data=conn.recv(2048)
        dofunc(data)
        conn.close()
    return


if __name__=='__main__':
    busDataServer(0)
