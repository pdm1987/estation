# -*- coding: gbk -*-
'''
��ģ��ά������վ��IP��ַ��.
����վ�Ƶ�IP��ַ����table_IP.py����.

ά������վ��IP��ַ�����:
1.�޸Ķ�Ӧ��ŵ�վ�Ƶ�IP��ַ

���ϲ���������table_IP�ṩ�Ĳ���.

�޸ĵ���վ�Ƶ�IP��ַ,ά��ģ��ͨ�����̵߳ķ�ʽ.
ÿ�β��������������̲߳���IP��ַ��.

ά��ģ������������վ�Ʒ�������ʱ����.
����ʱ��һ������վ��IP��ַ��.
'''


import _thread


class maintainIP:
    def __init__(self,  ip_table):
        self.ip_table=ip_table
    '''
    restoreIP����������һ�����߳�,�����ڲ�����_restoreIP��������
    '''
    def restoreIP(self, num, ip):
        _thread.start_new_thread(self._restoreIP, (num, ip))
        return
    
    def _restoreIP(self, num, ip):
        self.ip_table.setIP(num, ip)
        '''
        �ڲ��Ե�ʱ��ÿ�����ip����ip tableд�뵽�ļ���
        �ǲ���ʱ��д���ļ�ע��
        '''
        self.ip_table.writeToFile()
        return


if __name__=='__main__':
    from table_IP import table_IP
    def test():
        iptable=table_IP()
        mip=maintainIP(iptable)
        for i in range(10):
            mip.restoreIP(i,  '127.0.0.1')
        return
    test()
