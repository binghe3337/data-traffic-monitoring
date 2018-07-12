#!/usr/bin/python
#coding=utf-8
import sys,re,time,os
netcard = '/proc/net/dev'
nc = netcard or '/proc/net/dev'
fd = open(nc, "r")
netcardstatus = False
for line in fd.readlines():
    if line.find("eth0") > 0:
        netcardstatus = True
        field = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        field = line.split()
        print 'field[0]'
        print field[0]
        print 'field[1]'
        print field[1]
        print 'field[2]'
        print field[2]
        print 'field[3]'
        print field[3]
        print 'field[4]'
        print field[4]
        print 'field[5]'
        print field[5]
        print 'field[6]'
        print field[6]
        print 'field[7]'
        print field[7]
        print 'field[8]'
        print field[8]
        print 'field[9]'
        print field[9]
        print 'field[10]'
        print field[10]
        print 'field[11]'
        print field[11]
        print 'field[12]'
        print field[12]
        print 'field[13]'
        print field[13]
        print 'field[14]'
        print field[14]
        print 'field[15]'
        print field[15]
        print 'field[16]'
        print field[16]
        print 'field[17]'
        print field[17]
        print 'field[18]'
        print field[18]
        print 'field[19]'
        print field[19]
        print 'field[20]'
        print field[20]
if not netcardstatus:
    fd.close()
    print 'Please setup your netcard'
    sys.exit()
fd.close()
