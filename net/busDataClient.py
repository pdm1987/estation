# -*- coding: gbk -*-
'''
��busDataServer���͹���������
�涨������GPS���ݰ���ʽ���£�
    ����ͷ ������ID ������· ��γ�� У��� ����β
    ����ͷ������1�ֽ�,0x55
    ������ID������4�ֽڣ�ASCII��ʾ
    ������·������4�ֽڣ�ASCII��ʾ
    ��·�����У�����4�ֽ�
    ��γ�ȣ�16�ֽڣ�ǰ8���ֽ�Ϊ���ȣ���8���ֽ�Ϊγ��
    У��ͣ�����1�ֽڣ�������ID��������·�;�γ�Ȱ�λ���Ľ��
    ����β������1�ֽڣ�0xaa
�����ܳ���Ϊ31���ֽ�
'''

'''
���ݲ���
�����ԣ���ȷ(ud)��������ͷ(nh)��������β(ne)�����ݳ��Ȳ���(le)
��ȷ�ԣ���ȷ(ud)��У��ͳ���(ce)
��Ч�ԣ���ȷ(ud)����·��(ud)��������(ud)����γ�ȳ���Χ(ud)
'''

import socket
import network
from globalValues import BUS_DATA_LEN
from globalValues import BUS_DATA_HEAD
from globalValues import BUS_DATA_END
from utils import crc_check

def sendDataTCP(b_data):
    print(b_data)
    try:
        sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #print('socket')
        sock.connect((network.REMOTE_HOST, network.PORT_OF_BUSGPS))
        #print('connect')
        sock.send(b_data)
        #print('send')
        sock.close()
    except Exception as e:
        print('Error!', e)
    return

def constructData(id, line, stream, lng, lat):
    b_id=bytes(id, 'gbk')
    b_line=bytes(line.rjust(4), 'gbk')
    b_stream=bytes(stream, 'gbk')
    b_lng=bytes(lng, 'gbk')
    b_lat=bytes(lat, 'gbk')
    
    if len(b_id)!=4:
        print('bus id len should be 4')
        return b''
    if len(b_line)>4:
        print('line name should less than 5')
        return b''
    if len(b_stream)!=4:
        print('line stream should be ���� or ����')
        return b''
    if len(b_lng)!=8 or len(b_lat)!=8:
        print('len of lng/lat should be 8')
        return b''
    
    data=bytearray(BUS_DATA_LEN)
    data[0]=BUS_DATA_HEAD
    data[1:5]=b_id
    data[5:9]=b_line
    data[9:13]=b_stream
    data[13:21]=b_lng
    data[21:29]=b_lat
    data[-2]=crc_check(data[1:-2])
    data[-1]=BUS_DATA_END
    return data