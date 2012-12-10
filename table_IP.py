# -*- coding: gbk -*-
'''
����վ��IP��ַ�ı�.
    �ñ��������վ�Ʊ�������վ�Ƶ�IP��ַ��һһ��Ӧ�Ĺ�ϵ
    ����վ�Ʊ���ǵ���վ�Ƶ�Ψһ��ʶ,�ڵ���վ���ֳ�ʩ��ʱ��������.
    ����վ�Ƶı�ŷ�Χ��1~9999.
    ����һ������Ϊ10000�����鹹��.
    ������±��ʾ����վ�Ƶı��,�����е������Ƕ�Ӧ��ŵ�վ�Ƶ�IP��ַ.
    �ṩ���²���:
    1.�޸Ķ�Ӧ��ŵ�վ�Ƶ�IP��ַ
    2.��ȡ��Ӧ��ŵ�վ�Ƶ�IP��ַ
    3.��������д���ļ���
'''
import logging


TABLE_LENGTH=10000
INIT_IP='0.0.0.0'
IP_TABLE_FILENAME='IPtable.txt'


class table_IP:
    
    def __init__(self):
        self.table = [INIT_IP] * TABLE_LENGTH
        #logging.basicConfig(level=logging.INFO, 
        #        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',)
        #print(len(self.table))
    
    def setIP(self, num,  ip):
        if num >0 and num <TABLE_LENGTH:
            self.table[num]=ip
            logging.info("set IP %d %s"%(num, ip))
        return
    
    def getIP(self, num):
        if num > 0 and num < TABLE_LENGTH:
            return self.table[num]
        else:
            return INIT_IP
    
    def writeToFile(self,  filename=IP_TABLE_FILENAME):
        outfile=open(filename, 'w')
        for i in self.table:
            outfile.write(i)
            outfile.write('\n')
            outfile.flush()
        outfile.close()
        return
    
    '''��ȡ�ļ�'''
    def readFromFile(self, filename=IP_TABLE_FILENAME):
        infile=open(filename, 'r')
        i=0
        while True:
            s=infile.readline()
            s=s.rstrip('\n')
            if s=='':
                break
            else:
                self.setIP(i, s)
            i+=1
        infile.close()
        return


def test():
    #logging.basicConfig(level=logging.INFO, format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',)
    iptable = table_IP()
    iptable.setIP(1, "192.168.1.0")
    ip = iptable.getIP(1)
    print(ip)
    iptable.writeToFile()
    
    iptable2 = table_IP()
    iptable2.readFromFile()
    iptable2.writeToFile('tmp.txt')
    return

if __name__=='__main__':
    test()
