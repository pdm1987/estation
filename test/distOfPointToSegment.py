# -*- coding: gbk -*-
from math import sqrt
from distOfPointToPoint import distOfPointToPoint

#�����C���߶�AB�ľ���,��A,B,C�е�ֵ���Ǿ�γ��
def distOfPointToLineSegment(pA, pB, pC):
    #���ڼ���ĵ���붼�ܽ�,���Խ�3���㿴��һ��ƽ����
    dist=0
    a=distOfPointToPoint(pA, pB)
    b=distOfPointToPoint(pC, pB)
    c=distOfPointToPoint(pA, pC)
    
    if a == 0:
        dist=b
        return dist
    
    #�����C��ֱ��AB�ľ���
    ##x=��(2(a^2 b^2+a^2 c^2+b^2 c^2)-(a^4+b^4+c^4))/2a
    tmp=2*(a**2*b**2 + a**2*c**2 + b**2*c**2) - (a**4 + b**4 + c**4)
    if tmp < 0:
        x=0
    else:
        x=sqrt(tmp) / (2 * a)
    #print(x)
    
    #�жϹ���C���Ĵ�����ֱ��AB�Ľ���D�Ƿ����߶�AB��
    #�����߶�AD��BD�ĳ���,��AD > AB �� BD > AB,�򽻵�D�ڲ��߶�AB��
    ##AD^2+x^2=AC^2
    ##BD^2+x^2=BC^2
    tmp=c**2-x**2
    if tmp < 0:
        AD=0
    else:
        AD=sqrt(tmp)
    tmp=b**2-x**2
    if tmp < 0:
        BD=0
    else:
        BD=sqrt(tmp)
    
    if AD > a or BD > a:
        dist=min((b, c))
    else:
        dist=x
    return dist

############################################################


############################################################
if __name__=='__main__':
    print('test')
