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
import _thread
from busCalculate import busInfo

FILENAME='busData.txt'
file=None


def exit_server():
    global file
    file.close()
    return


def write_to_file(data):
    file.write(data)
    file.flush()
    return

funclist=[write_to_file]

def crc_check(b_data):
    if len(b_data)==0:
        return 0
    crc=b_data[0]
    for i in b_data[1:]:
        crc^=i
    return crc

'''
�ж����������Ժ�У��͵���ȷ��
'''
def check_data(data):
    '''
    ���ҵ�����ͷ
    '''
    i=0
    while i < len(data):
        if data[i]==0x55:
            '''��������β'''
            if data[i+BUS_DATA_LEN-1]==0xaa:
                '''�ж�У���'''
                checksum=data[i+BUS_DATA_LEN-2]
                cc=crc_check(data[i+1:i+BUS_DATA_LEN-2])
                if cc == checksum:
                    bus=busInfo()
                    bus.readDataPackage(data[i+1:i+BUS_DATA_LEN-2])
                    return bus
                else:
                    return None
            else:
                return None
        i+=1
    
    return None

'''
���ղ�Ԥ��������GPS����,�����ͷ����ؽ��
�涨������GPS���ݰ���ʽ���£�
    ����ͷ ������ID ������· ��γ�� У��� ����β
    ����ͷ������1�ֽ�,0x55
    ������ID������4�ֽڣ�ASCII��ʾ
    ������·������4�ֽڣ�ASCII��ʾ
    ��γ�ȣ�16�ֽڣ�ǰ8���ֽ�Ϊ���ȣ���8���ֽ�Ϊγ��
    У��ͣ�����1�ֽڣ�������ID��������·�;�γ�Ȱ�λ���Ľ��
    ����β������1�ֽڣ�0xaa
�����ܳ���Ϊ27���ֽ�
Ԥ�����ж�����У����Ƿ���ȷ
'''
BUS_DATA_LEN=27
def handleBusData(conn, addr, dofunc):
    print('Connected by ',  addr)
    '''
    ��������
    '''
    data=conn.recv(2048)
    '''
    �������
    '''
    ret=check_data(data)
    if ret != None:
        dofunc(data)
    conn.close()
    return

'''
����:
    flag:0 д���ļ� 1.���ú���
'''
def busDataServer(flag):
    global file
    running=True
    
    dofunc=funclist[flag]
    
    try:
        file=open(FILENAME, 'ab')
    except IOError:
        print('open file error')
    else:
        print('open file ok')
        atexit.register(exit_server)
    
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((network.HOST_OF_BUSGPS, network.PORT_OF_BUSGPS))
    sock.listen(1)
    while running:
        conn, addr=sock.accept()
        _thread.start_new_thread(handleBusData, (conn, addr, dofunc))
    return


if __name__=='__main__':
    busDataServer(0)
