# -*- coding: gbk -*-
'''
infoSending�ṩ����Ľӿ�
'''

import socket
import network

def __infoSendToServer(str):
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((network.REMOTE_HOST, network.PORT_OF_NETCONFIG))
    sock.send(bytes(str, 'gbk'))
    re=sock.recv(1024)
    sock.close()
    return re


def send_line(num, No, pool):

    return

def send_text(R_No, name, msg1, msg2, No, pool):

    return

def send_clear_text(R_No, No, pool):

    return

#��ʾ��ʽ,�ٶ�,ͣ��ʱ������
def send_speed(type, speed, stop, No, pool):

    return

#�����Ļ
def send_clear(No, pool):

    return
