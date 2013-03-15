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
from connectPool import connectPool
from busCalculate import busCalculate
from net.busDataServer  import busDataServer
from heartBeatServer import heartBeatServer
from infoSendingServer import infoSendingServer

from globalValues import bus_pos_dt


def init():
    bus_pos_dt
    
    
    #bus_pos_dt.insertNewBus(7704, ('2', '����'), 5)
    bus_pos_dt.print()
    return

from globalValues import initalGlobalValues
initalGlobalValues()


def mainServer():
    
    pool=connectPool()
    
    #_thread.start_new_thread(busDataServe, (0, ))
    #_thread.start_new_thread(reciveHeartBeat, (pool, ))
    #_thread.start_new_thread(netConfigServer, (pool, ))
    
    busdataserver=busDataServer(busCalculate.calculateBusPosition)
    busdataserver.start()
    
    heartbeatserver=heartBeatServer(pool)
    heartbeatserver.start()
    
    infosendingserver=infoSendingServer(pool)
    infosendingserver.start()
    return


if __name__=='__main__':
    init()
    #mainServer()
