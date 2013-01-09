# -*- coding: gbk -*-
'''
����������
    ����׼����
    1.�������ӳ�
    �������
    1.������GPS���ݽӿڷ���
    2.վ���������շ���
    3.�û����Ʒ���
'''
import _thread
from connectPool import connectPool
from busCalculate import busCalculate
from busDataServer  import busDataServer
from heartBeatServer import heartBeatServer
from netConfigServer import netConfigServer



def mainServer():
    
    pool=connectPool()
    
    #_thread.start_new_thread(busDataServe, (0, ))
    #_thread.start_new_thread(reciveHeartBeat, (pool, ))
    _thread.start_new_thread(netConfigServer, (pool, ))
    
    busdataserver=busDataServer(busCalculate.calculateBusPosition)
    busdataserver.start()
    
    heartbeatserver=heartBeatServer(pool)
    heartbeatserver.start()
    
    return


if __name__=='__main__':
    mainServer()
