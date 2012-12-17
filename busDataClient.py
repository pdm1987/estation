# -*- coding: gbk -*-
'''
��busDataServer���͹���������
�涨������GPS���ݰ���ʽ���£�
    ����ͷ ������ID ������· ��γ�� У��� ����β
    ����ͷ������1�ֽ�,0x55
    ������ID������4�ֽڣ�ASCII��ʾ
    ������·������4�ֽڣ�ASCII��ʾ
    ��γ�ȣ�16�ֽڣ�ǰ8���ֽ�Ϊ���ȣ���8���ֽ�Ϊγ��
    У��ͣ�����1�ֽڣ�������ID��������·�;�γ�Ȱ�λ���Ľ��
    ����β������1�ֽڣ�0xaa
�����ܳ���Ϊ27���ֽ�
'''

import socket
import network

def crc_check(b_data):
    if len(b_data)==0:
        return 0
    crc=b_data[0]
    for i in b_data[1:]:
        crc^=i
    return crc

def busDataClient():
    bus_id=bytes(str(7023), 'utf8')
    line=bytes(str(303).rjust(4), 'utf8')
    lng=bytes(str(70922263), 'utf8')
    lat=bytes(str(20374106), 'utf8')
    
    data=bytearray(27)
    data[0]=0x55
    data[1:5]=bus_id
    data[5:9]=line
    data[9:17]=lng
    data[17:25]=lat
    data[25]=crc_check(data[1:25])
    data[26]=0xaa
    
    print(data)
    print(data[1:25])
    
    try:
        sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('socket')
        sock.connect((network.REMOTE_HOST, network.PORT_OF_BUSGPS))
        print('connect')
        sock.send(data)
        print('send')
        sock.close()
    except:
        print('error')
    print('exit')
    return

if __name__=='__main__':
    busDataClient()
