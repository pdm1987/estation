# -*- coding: gbk -*-
'''
infoSending�ṩ����Ľӿ�
'''

import socket
import network
from globalValues import CMD_SET_TOTAL_ROAD
from globalValues import CMD_SET_LINE_TXT
from globalValues import CMD_SET_SPEED
from globalValues import CMD_CLEAR_LINE_TXT
from globalValues import CMD_CLEAR_ALL

def __infoSendToServer(s_data):
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((network.REMOTE_HOST, network.PORT_OF_INFOSENDING))
    sock.send(bytes(s_data, 'gbk'))
    re=sock.recv(1024)
    sock.close()
    return re

#���ù���վ��·����
#������st_id ����վ��ţ�num ��·����
def set_total_road(st_id, total):
    s_data=CMD_SET_TOTAL_ROAD+'\t'+str(st_id)+'\t'+str(total)
    __infoSendToServer(s_data)
    return

#���õ���վ����Ϣ
#������st_id ����վ��ţ�r_num ��·�ڸ�վ��ţ�r_name ��·����msg1 ������Ϣ��msg2 ������Ϣ
def set_line_text(st_id, r_num, r_name, msg1, msg2):
    s_data=CMD_SET_LINE_TXT+'\t'+str(st_id)+'\t'+str(r_num)+'\t'+str(r_name)+'\t'+str(msg1)+'\t'+str(msg2)
    __infoSendToServer(s_data)
    return

#���վ��ĳ·��Ϣ
#������st_id ����վ��ţ�r_num ��·�ڸ�վ���
def clear_line_text(st_id, r_num):
    s_data=CMD_CLEAR_LINE_TXT+'\t'+str(st_id)+'\t'+str(r_num)
    __infoSendToServer(s_data)
    return

#������ʾ��ʽ,�ٶ�,ͣ��ʱ��
#������st_id ����վ��ţ�type ��ʾ��ʽ,speed �ٶ�,stop ͣ��ʱ��
def set_speed(st_id, type, speed, stop):
    s_data=CMD_SET_SPEED+'\t'+str(st_id)+'\t'+str(type)+'\t'+str(speed)+'\t'+str(stop)
    __infoSendToServer(s_data)
    return

#�����Ļ
#������st_id ����վ���
def clear_all(st_id):
    s_data=CMD_CLEAR_ALL+'\t'+str(st_id)
    __infoSendToServer(s_data)
    return

if __name__=='__main__':
    print('test')
    set_total_road(1, 4)
    set_line_text(1, 1, '104', 'ͨ�� 3վ', '���� 5վ')
    clear_line_text(1, 1)
    set_speed(1, 1, 5, 25)
