# -*- coding: gbk -*-

'''
crc У��ͣ�������bytesArray������У���(��λ���)
'''

def crc_check(b_data):
    if len(b_data)==0:
        return 0
    crc=b_data[0]
    for i in b_data[1:]:
        crc^=i
    return crc
