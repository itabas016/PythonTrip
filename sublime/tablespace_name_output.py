#!/usr/bin/env python
#-*- coding:utf-8 -*-
tbresult=[]

def a():
        with open('tablespace_ecu_hansen.txt', 'rb') as tpr:
                for line in tpr:
#                       print line
                        array = line.split(" ")
                        print array
                        if len(array) > 5 and array[2] == 'TABLESPACE':
                                if array[3] in tbresult:
                                        pass
                                else:
                                        tbresult.append(array[3])

        with open('result_tablespace_ecu_hansen.txt', 'a') as tpw:
                for tname in tbresult:
                        tpw.write(tname + '\n')

a()