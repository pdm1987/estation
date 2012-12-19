# -*- coding: gbk -*-
'''
服务主程序
    数据准备：
    1.心跳连接池
    对外服务：
    1.公交车GPS数据接口服务
    2.站牌心跳接收服务
    3.用户控制服务
'''
import _thread
from connectPool import connectPool

from busDataServer  import busDataServe
from heartBeatServer import reciveHeartBeat
from netConfigServer import netConfigServer
def mainServer():
    
    pool=connectPool()
    
    _thread.start_new_thread(busDataServe, (0, ))
    _thread.start_new_thread(reciveHeartBeat, (pool, ))
    _thread.start_new_thread(netConfigServer, (pool, ))
    
    return


if __name__=='__main__':
    mainServer()
