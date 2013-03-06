# -*- coding: gbk -*-
'''
����վ��Ϣ��:
    ���е�һ������վ����Ϣ����:
    ����վ��(�򹫽�վid) ����վ�Ʊ�� ��·1 [��·2, ...]
    
    ����վ��(�򹫽�վid):
    Ψһ��ʶ�ù���վ,����ʹ��վ��(ԭ�������ֳ����õ���վ��ʱ����վ����ֱ��)
    ͬ����վ����������,����������
    
    ����վ�Ʊ��:
    ����վ�Ƶ�Ψһ��ʶ,�ڵ���վ���ֳ�ʩ��ʱ��������.
    ����վ�Ƶı�ŷ�Χ��1~9999.
    
    ��·1 [��·2, ...]:
    ������·������������·����.
    �г�������·������.��·������Ҫ��4���ֽڷ�Χ��.�����4����ĸ���ֻ����2�����ֻ����2����ĸ���ֺ�1���������.
    
    ʾ��:
    ������(����) 1192 1· 7· 302 ��5
    
    �ṩ�Ĳ���:
    1.���һ��������վ��Ϣ
    2.ͨ�����ֲ���һ��������վ����Ϣ
    3.ͨ����Ų���һ��������վ����Ϣ
    4.ͨ�������޸�һ��������վ�ı��
'''

BUSSTOPFILE='busStopTable.txt'


class busStopInfo:
    def __init__(self, name='',  num=1, *lines):
        self.name=name
        self.num=num
        self.lines=lines
        return
    
    def getName(self):
        return self.name
    
    def getNum(self):
        return self.num
    
    def getLines(self):
        return self.lines

    def getLineNum(self):
        return len(self.lines)

    def setName(self, name):
        self.name=name
    
    def setNum(self, num):
        self.num=num
        
    def setLines(self, lines):
        self.lines=lines


class table_busStop:
    def __init__(self):
        self.table=[]
        return
    
    def len(self):
        return self.table
    
    def index(self,  index):
        return self.table[index]
    
    def add(self, info):
        ##!!�Ժ���Ҫ�޸�,��ͬ��ŵ�Ӧ�ø���
        self.table.append(info)
        return
    
    def findByName(self, name):
        for info in self.table:
            iname=info.getName()
            if iname==name:
                return info
        return None
    
    def findbyNum(self, num):
        for info in self.table:
            inum=info.getNum()
            if inum==num:
                return info
        return None
    
    def changeNumByName(self, name, num):
        for info in self.table:
            iname=info.getName()
            if iname==name:
                info.setNum(num)
        return
    
    def printTable(self):
        for info in self.table:
            print('%s %d'%(info.getName(), info.getNum()), end='')
            for i in info.getLines():
                print(' %s'%(i), end='')
            print()
    
    def writeToFile(self, filename=BUSSTOPFILE):
        ofile=open(filename,  'w')
        s=''
        for info in self.table:
            s+=info.getName()+'\t'
            s+=str(info.getNum())
            for i in info.getLines():
                s+='\t'+str(i)
            s+='\n'
        ofile.write(s)
        ofile.close()
    
    def readFromFile(self, filename=BUSSTOPFILE):
        infile=open(filename, 'r')
        while True:
            s=infile.readline()
            s=s.rstrip('\n')
            if s=='':
                break
            else:
                arr=s.split('\t')
                print(arr)
                info=busStopInfo(arr[0], int(arr[1])) #ֱ�ӽ�lines��Ϊ��������������������,ʹ��setLines
                info.setLines(arr[2:])
                self.add(info)
        infile.close()
        return

if __name__=='__main__':
    def test():
        print('test')
        info = busStopInfo('������', 1, '1·', '2·', '302', '��4')
        print(info.getLines())
        info.setLines(('1·', '5·'))
        print(info.getLines())
        info.setLines(('1·', '4·'))
        print(info.getLines())
        
        busstoptable=table_busStop()
        busstoptable.add(info)
        busstoptable.printTable()
        busstoptable.writeToFile()
        busstoptable1=table_busStop()
        busstoptable1.readFromFile()
        busstoptable1.printTable()
        busstoptable1.writeToFile('tmp.txt')
    test()
