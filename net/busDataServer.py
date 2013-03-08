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
import threading
from utils import crc_check
from busCalculate import busInfo
from globalValues import BUS_DATA_LEN
from globalValues import BUS_DATA_HEAD
from globalValues import BUS_DATA_END

'''
�ж����������Ժ�У��,����ȷ�Ժ�������Ч��
����ֵ0�������,1������ȷ
'''
def check_data(data):
    if len(data)!=BUS_DATA_LEN:
        print('error data len')
        return 0
    if data[0]!=BUS_DATA_HEAD:
        print('error data head')
        return 0
    if data[-1]!=BUS_DATA_END:
        print('error data end')
        return 0
    if data[-2]!=crc_check(data[1:BUS_DATA_LEN-2]):
        print('error data checksum')
        return 0
    #������id�ж�
    #id=str(data[1:5],'gbk')
    #��������·�ж�
    #line=str(data[5:9],'gbk').strip()
    stream=str(data[9:13], 'gbk')
    if stream !='����' and stream!='����':
        print('line stream error, should be ���� or ����')
        return 0
    #��������γ���ж�
    lng=float(str(data[13:21], 'gbk'))/600000
    if lng < 110 or lng > 120:
        print('lng %f error,out bound [110,120]'%lng)
        return 0
    lat=float(str(data[21:29], 'gbk'))/600000
    if lat < 30 or lat >40:
        print('lat %f error,out bound [30,40]'%lat)
        return 0
    return 1

'''
Ԥ��������GPS����Ϊbus_info
'''
def pretreatData(b_data):
    bus=busInfo()
    bus.readDataPackage(b_data[1:BUS_DATA_LEN-2])
    return bus
###########################################

class handleBusData(threading.Thread):
    def __init__(self, conn, addr, cal_handle):
        threading.Thread.__init__(self)
        self.conn=conn
        self.addr=addr
        self.cal_handle=cal_handle
    
    def run(self):
        print('Connected by', self.addr)
        b_data=self.conn.recv(2048)
        print(b_data)
        r_ok=check_data(b_data)
        if r_ok:
            bus_info=pretreatData(b_data)
            self.cal_handle(bus_info)
        self.conn.close()
        return

class busDataServer(threading.Thread):
    def __init__(self, cal_handle):
        threading.Thread.__init__(self)
        self.cal_handle=cal_handle
        self.running=True
        self.thread_arr=[]
        return
    
    def run(self):
        print('busDataServer Start!')
        sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((network.HOST_OF_BUSGPS, network.PORT_OF_BUSGPS))
        sock.listen(1)
        while self.running:
            conn, addr=sock.accept()
            new_t=handleBusData(conn, addr, self.cal_handle)
            new_t.start()
            self.thread_arr.append(new_t)
        return
    
    def stop(self):
        self.running=False
        for t in self.thread_arr:
            t.join()
