# -*- coding: gbk -*-
from math import sin
from math import cos
from math import acos
from math import pi

EARTH_RADIUS=6371.004 #��λkm
R=EARTH_RADIUS

#�����A�͵�B���������,��A,B��ֵ�Ǿ�γ��
def distOfPointToPoint(pA, pB):
    lngA, latA=float(pA[0])*pi/180, float(pA[1])*pi/180
    lngB, latB=float(pB[0])*pi/180, float(pB[1])*pi/180
    
    #Ԥ����
    #��γȡ90-γ��ֵ(90- Latitude)����γȡ90+γ��ֵ(90+Latitude)
    #���ﶼ�Ǳ�γ,Ҳû���ϱ�γ��Ϣ���ڴ���,�Ժ���ܻ����
    
    '''
    ##��C����ֵ = sin(LatA)*sin(LatB) + cos(LatA)*cos(LatB)*cos(MLonA-MLonB)
    '''
    C=sin(latA)*sin(latB)+cos(latA)*cos(latB)*cos(lngA-lngB)
    
    '''
    ##ע��:C��ֵ��ʵ������ͼ��㾫��Ӱ��,C��ֵ�Ƿ���arcos�Ķ�����ȡֵ��Χ��[-1,1]
    '''
    #print('%1.30f'%C)
    if C > 1:
        print('C>1')
        C=1
    if C < -1:
        print('C<-1')
        C=-1
    
    dist=R*acos(C)
    return dist

#####################################################
TEST_FILE='pointToPoint_test.txt'
OUT_FILE='pointToPoint_result.txt'

def readTestFile():
    outfile=open(OUT_FILE, 'w')
    infile=open(TEST_FILE, 'r')
    while True:
        ss=infile.readline()
        ss=ss.strip('\t')
        if ss=='':
            break
        arr=ss.split('\t')
        pA=(arr[0], arr[1])
        pB=(arr[2], arr[3])
        dist=distOfPointToPoint(pA, pB)
        outfile.write(str(dist)+'\n')
    
    infile.close()
    outfile.close()
    return

#####################################################

if __name__=='__main__':
    readTestFile()
    print('test')
