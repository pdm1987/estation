# -*- coding: gbk -*-
'''
busCalculate.py ���㹫��������·�ϵ�λ��.

���ݸù���������·�͹�����������,ȷ������������·�ϵ�λ��

����:
    lineTable ---- ��·���б�
    lineDistTable ---- ��·�����б�,��lineDistance.py����
    busInfo ----��������Ϣ

����:
    lineBusTable----���������λ�ù�����λ�õ���·
    
busInfo ��������Ϣ:
    ��id,������·����,����,γ��
    
lineBusTable :
    lineBusTable�е���·��lineTable�е���·һһ��Ӧ,
    ����ÿ����·�ǰ������������·��λ�õĹ���������·

lineBusLine :
    ���������·��λ�õĹ���������·,��lineBusTable�е�һ��Ԫ��
    LineBusLine��һ��List,����elemOfLineBus
    �ṩ�Ĳ���:
    1.����վ������,���ص�һ�������վ�����վ��վ��
    2.����վ������,���ص�һ�������վ�����վ�ľ���
    3.����վ������,����ǰ���������վ�����վ��վ��
    4.����վ������,����ǰ���������վ�����վ��վ��
    
elemOfLineBus:
    elemOfLineBus ��������Ϣ
    1.վ������/id,��վ��վ������/idΪ'-1'
    2.��վ����һվ�ľ���
    3.��һվ����վ�Ĺ�����
    
    �ṩ�Ĳ���:
    1.���ݹ�������,����վ�����һ��������
    2.���ݹ�������,�Ӹ�վ��ɾ��һ��������
    
'''

class busInfo:
    def __init__(self, id, lineName, lng, lat):
        self.id=id
        self.lineName=lineName
        self.lng=lng
        self.lat=lat
    
    def readDataPackage(self, dataPack):
        #����dataPackage �е����ݸ�ʽ��ȷ����ȡ�ķ���
        return
    
    def getLineName(self):
        return self.lineName

class busInfo_cal():
    def __init__(self, id, line, station, dist):
        self.id=id
        self.line=line
        self.station=station
        self.dist=dist
    
    def getLine(self):
        return self.line
    
    def getStation(self):
        return self.station
    
    def getDist(self):
        return self.dist
    
    def setLine(self, line):
        self.line=line
    
    def setStation(self, station):
        self.station=station
    
    def set(self, info):
        self.line=info.line
        self.station=info.station
        self.dist=info.dist

#���ڼ�¼��������Ϣ�ı�
class busInfoTable():
    def __init__(self):
        self.table=list()
    
    def findById(self, id):
        for info in self.table:
            if info.id == id:
                return info
        return None
    
    #add a businfo to table if the id of businfo not in table,
    #if not update the businfo status
    def update(self, info):
        oldinfo=self.findById(info)
        if oldinfo:
            oldinfo.set(info)
        else:
            #��Ӳ���ע������
            self.table.append(info)
        return

class elemOfLineBus:
    def __init__(self, name, dist):
        self.name=name
        self.dist=dist
        self.buses=[] ##list�д�ŵ���businfo��busId(or busindex in businfo)
        return
'''
Ԫ����һ��line,ÿ��line�е�Ԫ����elemOfLineBus
'''
class lineBusTable:
    def __init__(self):
        self.table=[]
    
    def addbus(self, busId, lineIndex, station):
        line=self.table[lineIndex]
        for st in line:
            if st.name==station:
                st.buses.append(busId)
                break
        return
    
    def delbus(self, busId, lineIndex, station):
        line=self.table[lineIndex]
        for st in line:
            if st.name==station:
                for bus in st.buses:
                    if bus==busId:
                        st.buses.remove(bus)
        return

###############################################
import lineDistance
import math


def maxAngleCos(a, b, c):
    sides=[a, b, c]
    maxs=max(sides)
    sides.remove(max(sides))
    e, f=0, 2
    for i in sides:
        e+=i**2
        f*=i
    C=(e-maxs**2)/f
    return C

'''
���幫�����������߶�AB��ĩ��B��̾���bed
    1.����������C��ֱ��AB�Ĵ��߽��ڵ�D,��D���߶�AB��,��DB��Ϊ����
    2.ͬ1������,�����㲻���߶�AB��,��CB�ڹ���Ϊ����
    
distOfBusToSegmentEnd ��������һ��Ԫ��(bed,dist)
bed ---- �������������߶�AB��ĩ��B��̾���
dist ---- ���������߶�AB�ľ���,�����lineDistance.py

'''
def distOfBusToSegmentEnd(bus, pA, pB):
    #���ڼ���ĵ���붼�ܽ�,���Խ�3���㿴��һ��ƽ����
    bed, dist=0, 0
    a=lineDistance.distOfPointToPoint(pA, pB)
    b=lineDistance.distOfPointToPoint(bus, pB)
    c=lineDistance.distOfPointToPoint(pA, bus)
    #print(a, b, c)
    '''
    ���ǵ����㾫�ȵ�����,��a,b,c����һ��С��r(r�ӽ�0),�򲻼���x,AD,BD
    ���⵱x��ֵС��r(��bus�ӽ�AB���ڵ�ֱ��),���㿪��Ҳ�����ھ��ȵ�������
    ����r��ʱȡ0.0001
    '''
    r=0.0001
    d=maxAngleCos(a, b, c)
    #print(a, b, c, d+1)
    if a < r:
        #print(1, a)
        bed=a
        dist=b
    elif b < r:
        #print(2, b)
        bed=b
        dist=b
    elif c < r:
        #print(3, c)
        bed=a
        dist=c
    ##���ǽӽ�180�����ǵ�cosֵ�ӽ�-1
    elif d - (-1)< r:
        #print(4, d+1)
        bed=b
        if a > b and a > c:
            dist=0
        else :
            dist=min(b, c)
    else :
        #�����C��ֱ��AB�ľ���
        ##x=��(2(a^2 b^2+a^2 c^2+b^2 c^2)-(a^4+b^4+c^4))/2a
        x=math.sqrt(2*(a**2*b**2 + a**2*c**2 + b**2*c**2) - (a**4 + b**4 + c**4)) / (2 * a)
        #print(5, x)
        #�жϹ���C���Ĵ�����ֱ��AB�Ľ���D�Ƿ����߶�AB��
        #�����߶�AD��BD�ĳ���,��AD > AB �� BD > AB,�򽻵�D�ڲ��߶�AB��
        ##AD^2+x^2=AC^2
        ##BD^2+x^2=BC^2
        AD=math.sqrt(c**2-x**2)
        BD=math.sqrt(b**2-x**2)
        if AD > a or BD > a:
            onAB=False
        else:
            onAB=True
    
        #����AD,BD��С�жϹ������������߶ε�ĩ�˾���
        if onAB:
            bed=BD
            dist=x
        else:
            bed=b
            dist=min((b, c))
    
    return bed, dist
'''
���㹫��������·����ʻ����һվ
����:
    lineDist ---- list of elemOfLineDist, elemOfLineDist��lineDistance.py
    busPoint ---- ��������γ��
����ֵ:
    position ---- (����������һվ����lineDist���±�,������һվ�ľ���)
'''

def calculateBusNextStation(lineDist, busPoint):
    minp2s=float('Infinity')
    bias=0
    dist=0
    for i in range(len(lineDist)-1):
        #print(i)
        pA=lineDist[i].getCoordinate()
        pB=lineDist[i+1].getCoordinate()
        
        #��������һ��Ԫ��(���������߶��յ�ľ���,�㵽�߶εľ���)
        ret=distOfBusToSegmentEnd(busPoint, pA, pB)
        p2s=ret[1]
        #print(ret, bias)
        #compare method of judge weather the bus in this segment,two way
        #1.the minimun dist
        #2.when the dist less than 
        if p2s < minp2s:
            minp2s=p2s
            bias=i
            dist=ret[0]
    #bias+1��������һվ
    return (bias+1, dist)


'''
���㹫��������·�ϵ�λ��
��ȡ��������������Ϣ(busInfo),��·�����������Ϣ(lineDistTable)
ͨ������,�ó���������һվ����һվ�;�����һվ�ľ���,
����������Ϣд��lineBusTable��
'''
def busPositionCalculate(lineDist, busInfo):
    #�����busInfo�е�bus����λ��
    busPoint=[busInfo.lng, busInfo.lat]
    position=calculateBusNextStation(lineDist, busPoint)
    return position

'''
����˵��:
1.position ---- �ڸ���·�ϵ�ƫ����,����һվ����
2.lineDist ---- ����·��վ�����
3.lineIndex ----����·����·���е�ƫ��
4.lineBusTable ---- ��·������,��Ҫ����lineIndex�ҵ����������ڵ���·
5.busInfoTable ---- ������Ϣ��,����������ԭ�����ڵ���·
'''
def updateTheLine(position, lineDist, lineIndex, lineBusTable, lineTable, busInfo, busInfoTable):
    #first update the lineBusTable,del old position,add new position
    busId=busInfo.id
    oldbus=busInfoTable.findById(busId)
    oldline=oldbus.getLine()
    oldstation=oldbus.getStation()
    oldlineIndex=lineTable.getIndexByName(oldline)
    
    newline=lineDistTable.index(lineIndex)
    newstation=newline[position[0]].getStationId()

    lineBusTable.delbus(busId, oldlineIndex, oldstation)
    lineBusTable.addbus(busId, lineIndex, newstation)
    
    #second get all station need update sending informateion and add to stationInfo
    ##call stationInfo func
    
    
    #third update busInfoTable
    bus_cal=busInfo_cal(busId, newline, newstation, position[1])
    busInfoTable.update(bus_cal)
    return
'''
���ݹ�������Ϣ������·��������ͼ����Ĺ�������Ϣ��
��·���������а���������·
ÿ����·�ϰ���վ��(��lineDistTable��վ��һ��)
ÿ��վ���¼����һվ�ľ���͵���վ�Ĺ�����id�б�

�����Ĺ�������Ϣ�� busInfo_cal
�������й������ļ�¼
ÿ����¼������������·�ͽ�Ҫ����վ

�������������λ�ú����ԭ����¼�ڼ����Ĺ�������Ϣ���иó�����Ϣ
������·��������,
���Ƚϼ����Ĺ�������Ϣ����ԭ����λ��,ȷ����Щվ����Ҫ���·����µ���Ϣ
�����¼����Ĺ�������Ϣ
'''
def updateLineBus(lineTable, lineDistTable, lineBusTable, busInfoTable, busInfo):
    lineName=busInfo.getLineName()
    lineIndex=lineTable.getIndexByName(lineName)
    lineDist=lineDistTable.index(lineIndex)
    #lineBus=lineBusTable(lineIndex)
    
    #��������һ��Ԫ��(����һվ��ƫ����,����һվ����)
    position=busPositionCalculate(lineDist, busInfo)
    
    #update line
    updateTheLine(position, lineDist, lineIndex, lineBusTable, lineTable, busInfo, busInfoTable)
    return

###############################################



if __name__=='__main__':
    from testBusFile import bus
    from lineDistance import lineDistTable
    print('test')
    bus1=bus()
    bus1.readFromFile('busone.txt')
    bus1.writeTofile('tmp3.txt')
    
    print("test distOfBusToSegmentEnd")
    ret=distOfBusToSegmentEnd((118.216117,33.963728), (118.214824,33.960854), (118.214824,33.960854))
    print(ret)
    
    
    print('test func calculateBusNextStation()')
    bus2=bus()
    bus2.readFromFile('bus2.txt')
    ldt=lineDistTable()
    ldt.read_from_file('linedist.txt')
    line=ldt.index(0)
    for i in bus1.path:
        pos=calculateBusNextStation(line, i)
        print(pos)
    
    print('exit')
