#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : data_helper.py
# @Author: nanzhi.wang
# @Date  : 2018/9/25 上午10:35
import numpy as np
import random as rd
class data_helper:
    def __init__(self,config):

        with open(config['train_file'],'r',encoding='utf-8') as train_file:
            data=[]
            for line in train_file.readlines():
                data.append([int(i) for i in line.rstrip().split(' ')[1:]])
            data=np.array(data)
            self.train_x=data[:,:-1]
            self.train_y=data[:,-1]


        with open(config['test_file'],'r',encoding='utf-8') as test_file:
            data = []
            for line in test_file.readlines():
                data.append([int(i) for i in line.rstrip().split(' ')[1:]])
            data = np.array(data)
            self.test_x = data[:, :-1]
            self.test_y = data[:, -1]
        self.batch_num=0
        self.random_strat=0

    def next_batch(self,size):
        train_x=self.train_x[(self.random_strat+self.batch_num)%len(self.train_x)*size:
                             min(self.random_strat+(self.batch_num+1)*size,len(self.train_x))%len(self.train_x)]
        train_y = self.train_y[(self.random_strat+self.batch_num)%len(self.train_y)*size:
                               min(self.random_strat+(self.batch_num+1)*size,len(self.train_y))%len(self.train_y)]
        self.batch_num+=1
        if self.batch_num>1000000:
            self.batch_num=0
        self.random_strat=rd.randint(0,self.batch_num-2)
        return train_x,train_y







