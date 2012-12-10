# -*- coding: gbk -*-
'''
���������յ���վ�Ƶ�������
    ����������Э����ָ���˿�����������,ͬʱ��ȡ�����������ĵ���վ���豸��IP��ַ
    ����������IP��ַ�����ݶԵ���ʽ���͸�IP��ά��ģ��
    
��������ʽ
    ����Ϊ4���ֽ�, ����:
    ��1����4���ֽڵ�0x30 0x30 0x30 0x31 �����ն˱����0001
    
������ղ���p��ӡiptable���ļ���
'''


import socket
import network
import _thread


def handleConnect(conn, pool):
    data=conn.recv(1024)
    print(data)
    num=0
    try:
        num=int(data[:4])
    except ValueError:
        print('handle Connect error, data %s'%(data[:4]))
    pool.addConn(num, conn)
    return

def reciveHeartBeat(pool):
    print(network.HOST_OF_HEARTBEAT)
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((network.HOST_OF_HEARTBEAT, network.PORT_OF_HEARTBEAT))
    s.listen(1)
    while True:
        conn, addr=s.accept()
        print('HeartBeat Connected by',  addr)
        t_id=_thread.start_new_thread(handleConnect, (conn, pool))
        print('handle connect thread id %d'%(t_id))
    return


if __name__=='__main__':
    #from maintainIP import maintainIP
    #from table_IP import table_IP
    from connectPool import connectPool
    import netConfigServer
    '''
    ���Գ�������һ��ip table, ����������reciveHeartBeat����
    ���񽫽��յ���ip д�뵽ip table��
    '''
    
    def test():
        #iptable=table_IP()
        #mip=maintainIP(iptable)
        pool=connectPool()
        #conn=None
        #_thread.start_new_thread(handleConnect, (conn, pool))
        _thread.start_new_thread(netConfigServer.netConfigServer, (pool, ))
        
        reciveHeartBeat(pool)
    
    test()
