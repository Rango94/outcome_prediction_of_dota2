#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : dis_the_data.py
# @Author: nanzhi.wang
# @Date  : 2018/9/29 上午11:26

import random as rd
import sys
fo_train=open('data_train','w',encoding='utf-8')
fo_test=open('data_test','w',encoding='utf-8')
fo_val=open('data_val','w',encoding='utf-8')


with open(sys.argv[1],'r',encoding='utf-8') as fo:
    for line in fo.readlines():
        if rd.random()>0.8:
            if rd.random()>0.5:
                fo_test.write(line)
            else:
                fo_val.write(line)
        else:
            fo_train.write(line)



