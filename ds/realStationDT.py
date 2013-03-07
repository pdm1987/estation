# -*- coding: gbk -*-
# auther : pdm
# email : ppppdm@gmail.com

# realStationDT.py
# This file define class realStationDT which store the distance or
# station count bus to the station in all bus line.
#
#   User can get all station's distance/station count information in 
# one line by line name in realStationDT.
#
#   And realStationDT will update line stations information by bus 
# position list, calculated before, in this line

class realStationDT:
    def __init__(self, l_names, l_st_nums):
        self.l_names = l_names
        self.l_st_nums = l_st_nums
        self.lines = list()
        for st_num in l_st_nums:
            bus_line = list()
            for i in range(st_num):
                bus_line.append(i)
            self.lines.append(bus_line)
    
    def print(self):
        print(self.l_names)
        print(self.lines)
    
    def getOneLine(self, line_name):
        i = 0
        for l_name in self.l_names:
            if l_name == line_name:
                return self.lines[i]
            i = i + 1
        # if don't have the line name list
        voidlist = list()
        return voidlist
    
    def updateLine(self, line_name, line_bus_pos, func_realStaionDist):
        # if have the line name list
        i = 0
        for l_name in self.l_names:
            if l_name == line_name:
                self.lines[i] = func_realStaionDist(line_bus_pos, self.l_st_nums[i])
                return
            i = i + 1
        # if don't have the line name list
        # we don't do anything as don't know the line station numbers
        return

if __name__=='__main__':
    print(__file__+' test')
    line_names = ['1', '2', '305']
    line_st_nums = [3, 4, 5]
    real_staton_dt = realStationDT(line_names, line_st_nums)
    real_staton_dt.print()
    
    #
    print(real_staton_dt.getOneLine('1'))
    print(real_staton_dt.getOneLine('202'))
    
    def dofunc(positions, station_numbers):
        # assume that position have already sorted
        return
