# -*- coding: gbk -*-
'''
���������յ���վ�Ƶ�������
    ����������Э����ָ���˿�����������,ͬʱ��ȡ�����������ĵ���վ���豸��IP��ַ
    ����������IP��ַ�����ݶԵ���ʽ���͸�IP��ά��ģ��
    
��������ʽ
    ����Ϊ4���ֽ�, ����:
    ��1����4���ֽڵ�0x30 0x30 0x30 0x31 �����ն˱����0001
'''


import socket
import network


HOST='localhost'


def reciveHeartBeat(mip):
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, network.PORT_OF_HEARTBEAT))
    s.listen(1)
    while True:
        conn, addr=s.accept()
        print('Connected by',  addr)
        data=conn.recv(4)
        if data:
            print(int(data))
            mip.restoreIP(int(data), addr[0])
            conn.sendall(b' ')
        conn.close()
    return


if __name__=='__main__':
    from maintainIP import maintainIP
    from table_IP import table_IP
    import _thread
    def print_ip_table(iptable):
        while True:
            s=input('Enter p to print IP table:')
            if s=='p':
                print('to print')
                break
        
        iptable.writeToFile()
    
    def test():
        iptable=table_IP()
        mip=maintainIP(iptable)
        _thread.start_new_thread(print_ip_table, (iptable, ))
        reciveHeartBeat(mip)
    
    test()
