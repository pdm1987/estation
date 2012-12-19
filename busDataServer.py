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
import _thread
from busCalculate import busInfo
from busCalculate import updateLineBus
from busCalculate import lineBusTable
from busCalculate import busInfoTable
from lineDistance import lineDistTable
from lineDistance import linesTable

from globalValues import BUS_DATA_LEN

FILENAME='busData.txt'
file=None


def write_to_file(businfo):
    try:
        file=open(FILENAME, 'w')
    except IOError:
        print('open file error')
    else:
        print('open file ok')
    s=''
    s+=businfo.id+'\t'+str(businfo.lineName)+'\t'+str(businfo.lng)+'\t'+str(businfo.lat)+'\n'
    file.write(s)
    file.flush()
    file.close()
    return

def printRet(businfo):
    s=businfo.id+'\t'+str(businfo.lineName)+'\t'+str(businfo.lng)+'\t'+str(businfo.lat)
    print(s)

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
                    print('error data checksum')
                    return None
            else:
                print('error data end')
                return None
        i+=1
    print('data no head 0x55')
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

lt=linesTable()
lt.read_from_file('lines.txt')

ldt=lineDistTable()
ldt.read_from_file('linedist.txt')

lbt=lineBusTable()
lbt.read_from_dist_file('linedist.txt')

bit=busInfoTable()

def handleBusData(conn, addr):
    print('Connected by ',  addr)
    '''
    ��������
    '''
    data=conn.recv(2048)
    print(data)
    '''
    �������
    '''
    ret=check_data(data)
    if ret != None:
        write_to_file(ret)
        printRet(ret)
        #updateLineBus(lineTable, lineDistTable, lineBusTable, busInfoTable, busInfo)
        updateLineBus(lt, ldt, lbt,bit,ret)
    conn.close()
    return

def busDataServer(flag):
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((network.HOST_OF_BUSGPS, network.PORT_OF_BUSGPS))
    sock.listen(1)
    while True:
        conn, addr=sock.accept()
        _thread.start_new_thread(handleBusData, (conn, addr))
    return


if __name__=='__main__':
    busDataServer(0)
