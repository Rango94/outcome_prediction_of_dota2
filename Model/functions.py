#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : functions.py
# @Author: nanzhi.wang
# @Date  : 2018/9/28 下午5:14

import numpy as np

def tostring(config):
    keys_ = config.keys()
    keys_.sort()
    return '-'.join([key + '_' + str(config[key]) for key in keys_])


def pre(pre_socre,truth):
    pre_socre=np.reshape(pre_socre,[-1])
    truth=np.reshape(truth,[-1])
    sum=0
    for i,j in zip(pre_socre,truth):
        i=int(i+0.5)
        if i==j:
            sum+=1

    return sum/len(pre_socre)

