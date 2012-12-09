# -*- coding: gbk -*-
'''
busStopClient.py ���ձ�׼�����е�busStopInfo�����������busStopInfo.

busStopClient ��������ձ�׼�����е�����
-i info          ����info,��ʽ:վ�� ��� ��·1 [��·2 ...]
-q               �˳�
-h               ��ʾ����

����busStopInfo��Ϣ���ж������Ƿ����Ҫ��.
����Ҫ�󽫰���Ϣ���͸������.
'''

import socket
import network


RUNNING=True

def deal_info(arr):
    print(arr)
    num=int(arr[1])
    if num <1 or num >9999:
        print_help(arr)
        return
    
    #send to Server
    msg=b''
    for i in arr:
        msg+=bytes(i, 'utf8')+b' '
    msg=msg[:-1]
    print(msg)
    
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((network.REMOTE_HOST,  network.PORT_OF_BUSSTOP))
    sock.sendall(msg)
    return

def exit_client(arr):
    global RUNNING
    RUNNING=False
    return
    
def print_help(arr):
    print('busStopClient help:')
    print('-i info          ����info,��ʽ:վ�� ��� ��·1 [��·2 ...]')
    return

cmd_list=[
          ['-i', deal_info],
          ['-q', exit_client], 
          ['-h', print_help]
          ]



print("BusStopClient Start")

while RUNNING:
    s=input('$ ')
    arr=s.split()
    for c in cmd_list:
        if arr[0]==c[0]:
            c[1](arr[1:])
            break

print("BusStopClient Exit")
