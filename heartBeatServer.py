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


HOST='localhost'


def reciveHeartBeat(pool):
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((network.HOST_OF_HEARTBEAT, network.PORT_OF_HEARTBEAT))
    s.listen(1)
    while True:
        conn, addr=s.accept()
        print('HeartBeat Connected by',  addr)
        data=conn.recv(1024)
        if data:
            print(int(data[:4]))
            pool.addConn(int(data[:4]), conn)
            #Don't close conn
    return


if __name__=='__main__':
    #from maintainIP import maintainIP
    #from table_IP import table_IP
    from connectPool import connectPool
    import netConfigServer
    import _thread
    '''
    ���Գ�������һ��ip table, ����������reciveHeartBeat����
    ���񽫽��յ���ip д�뵽ip table��
    '''
    def test():
        #iptable=table_IP()
        #mip=maintainIP(iptable)
        pool=connectPool()
        _thread.start_new_thread(netConfigServer.netConfigServer, (pool, None, ))
        
        reciveHeartBeat(pool)
    
    test()
