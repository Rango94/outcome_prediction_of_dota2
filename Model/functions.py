#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : functions.py
# @Author: nanzhi.wang
# @Date  : 2018/9/28 下午5:14



def tostring(config):
    keys_ = config.keys()
    keys_.sort()
    return '-'.join([key + '_' + str(config[key]) for key in keys_])
