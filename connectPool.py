# -*- coding: gbk -*-
'''
conncetPool.py ����վ�����ӳر�
    GPRSģ�鴦�����������������,��˷����������������ӵ�IP��ַ����������·�ɵ�IP��ַ.
��������û���������������վ�Ƶ����ӵ�.
    ���Ե���վ�Ʒ������������Ӻ���Ҫ�����ӱ��ֵ����ӳ���,ʹ��ʱ�����ӳ���ȡ�����������վ��ͨ��.
    ���table_IP.py(�����ӵ�IP��ַд���ļ���)��maintainIP.pyû������.
    
���ݽṹ:
    ��� ����
    
����:
    1.��һ�����Ӽ��뵽���ӳ���
    2.���ݱ�Ŵ����ӳ���ȡ������

ע��:
    ���õ��ϲ�Ӧ���жϸ������Ƿ�Ϊ��������,���������ӽ����ټ������ӳ���.
    
    ��Ȼ����ʧЧֻ�������ӳ��з���,���Է��ظ��ϲ�����ӿ�������Ч������
'''

class connectPool:
    def __init__(self):
        self.pool=dict()
    
    def addConn(self, num, coon):
        self.pool[num]=coon
        return
    
    def getConn(self, num):
        try:
            return self.pool.pop(num)
            #ʹ��pop ��coon�Ƴ�,�Է�����ʱ����������ʹ�õ�����
            #��Ȼ�����������ʹ���е����Ӳ������
        except KeyError:
            print('connectPool key error')
            return None
    
    def printPool(self):
        print(self.pool)

CONN_LIST_LENGTH=10000
INIT_CONN=None

class conncetList():
    def __init__(self):
        self.list=[INIT_CONN]*CONN_LIST_LENGTH
        return
    
    def get(self, num):
        print(len(self.list))
        return self.list[num]
    
    def set(self, num, conn):
        self.list[num]=conn
        return

if __name__=='__main__':
    a, b=1, 's'
    pool=connectPool()
    pool.addConn(a, b)
    pool.printPool()
    a, b=2,'c'
    pool.addConn(a,b)
    pool.printPool()
    print(pool.getConn(2))
    print(pool.getConn(3))
    pool.printPool()

    cl=conncetList()
    print(cl.get(0))
    print(cl.set(0, 'x'))
