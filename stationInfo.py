# -*- coding: gbk -*-
'''
station.py ����վ��Ϣ�б�

����վ��Ϣ�б�
    �������еĹ���վ,ÿ������վ�����˸�վӦ�е���·
    ��·��Ϣͨ��busCalculate.py������.
    
'''


'''
����վ��Ϣ
'''
class stopInfo:
    def __init__(self, id, name, lines):
        self.id=id
        self.name=name
        self.lines=lines
        self.info=[None]*len(self.lines)
        return
    
    def getId(self):
        return self.id
    
    def getName(self):
        return self.name
    
    def getLines(self):
        return self.lines

'''
��������վ��Ϣ
    ��վ��Ϣ����Ҫ��Ҫ�е�վ��վ��,����,�������,�������:
    1.��һ������վ�Ĺ����������վ��
    2.�ڶ�������վ�Ĺ����������վ��
    3.��һ������վ�Ĺ������������
    4.�ڶ�������վ�Ĺ������������
    5.����·����վ�Ƿ��쳣
    6.�쳣������͵���Ϣ
    ����������������
'''
class busToStopInfo():
    def __init__(self):
        self.fisrtNum=0
        self.secondNum=0
        self.firstStatus='����'
        self.secondStatus='����'
        self.isUnusual=0
        self.unusualInfo=' '
        return
