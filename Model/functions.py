#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : functions.py
# @Author: nanzhi.wang
# @Date  : 2018/9/28 下午5:14

import numpy as np
import random as rd
def tostring(config):
    keys_ = config.keys()
    keys_.sort()
    return '-'.join([key + '_' + str(config[key]) for key in keys_])


def Pre(pre_socre,truth):
    pre_socre=np.reshape(pre_socre,[-1])
    truth=np.reshape(truth,[-1])
    sum=0
    for i,j in zip(pre_socre,truth):
        i=int(i+0.5)
        if i==j:
            sum+=1

    return sum/len(pre_socre)


def auc(pre,truth):

    pre = np.reshape(pre, [-1])
    truth = np.reshape(truth, [-1])
    pre,truth=zip(*sorted(zip(pre,truth),key=lambda x:x[0]))
    x=0
    y=0
    kkk=sum(truth)
    auc=0
    for idx in range(len(pre)):
        x_=sum(truth[:idx])/kkk
        y_=(idx-sum(truth[:idx]))/kkk
        auc+=((y_+y)*(x_-x))/2
        x=x_
        y=y_

    return auc

if __name__=='__main__':
    pre=np.array([rd.random() if rd.random()>i else rd.random() for i in range(1000)])

    truth=np.array([0 if rd.random()<0.5 else 1 for _ in range(1000)])
    print(auc(pre,truth))
