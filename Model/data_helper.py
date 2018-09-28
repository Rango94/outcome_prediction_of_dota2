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
                tmp=[int(i) for i in line.rstrip().split(' ')[1:]]
                if len(tmp)!=11:
                    continue
                else:
                    data.append(np.array(tmp))

            data=np.array(data)
            self.train_x=data[:,:-1]
            self.train_y=data[:,-1]
        #
        # with open(config['test_file'],'r',encoding='utf-8') as test_file:
        #     data = []
        #     for line in test_file.readlines():
        #         data.append([int(i) for i in line.rstrip().split(' ')[1:]])
        #     data = np.array(data)
        #     self.test_x = data[:, :-1]
        #     self.test_y = data[:, -1]
        self.start=2000



    def next_batch(self,size):

        train_x=self.train_x[self.start:min(self.start+size,len(self.train_x))]
        train_y = self.train_y[self.start:min(self.start+size,len(self.train_y))]

        self.start+=size
        if self.start>len(self.train_x):
            self.start=2000

        return train_x,train_y


    def get_test_batch(self):

        train_x = self.train_x[:2000]
        train_y = self.train_y[:2000]

        return train_x, train_y



