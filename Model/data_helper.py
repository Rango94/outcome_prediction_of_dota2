#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : data_helper.py
# @Author: nanzhi.wang
# @Date  : 2018/9/25 上午10:35
import numpy as np
import random as rd
import codecs
class data_helper:
    def __init__(self,config):

        with codecs.open(config['train_file'],'r',encoding='utf-8') as train_file:
            data=[]
            for line in train_file.readlines():
                line=line.rstrip().split(' ')[1:]
                if len(line)!=11:
                    continue
                data.append([int(i) for i in line])
                data.append([int(line[idx%10]) if idx!=15 else 0 if line[-1]=='1' else 1 for idx in range(5,16)])
            data=np.array(data)
            self.train_x=data[:,:-1]
            self.train_y=data[:,-1]

        with codecs.open(config['test_file'],'r',encoding='utf-8') as test_file:
            data = []
            for line in test_file.readlines(): 
                line=line.rstrip().split(' ')[1:]
                if len(line)!=11:
                    continue
                data.append([int(i) for i in line])
            data = np.array(data)
            self.test_x = data[:, :-1]
            self.test_y = data[:, -1]

        with codecs.open(config['val_file'], 'r', encoding='utf-8') as val_file:
            data = []
            for line in val_file.readlines():
                line=line.rstrip().split(' ')[1:]
                if len(line)!=11:
                    continue
                data.append([int(i) for i in line])
            data = np.array(data)
            self.val_x = data[:, :-1]
            self.val_y = data[:, -1]

        self.start = 0


    def next_batch(self,size):

        train_x=self.train_x[self.start:min(self.start+size,len(self.train_x))]
        train_y = self.train_y[self.start:min(self.start+size,len(self.train_y))]

        self.start+=size
        if self.start>len(self.train_x):
            self.start=0

        return train_x,train_y


    def get_test_batch(self):
        return self.test_x, self.test_y


    def get_val_batch(self):
        return self.val_x, self.val_y



