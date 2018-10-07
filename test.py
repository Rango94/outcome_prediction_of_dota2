from Model.functions import auc
import random as rd
import numpy as np
from sklearn import metrics

pre=np.array([rd.random() for i in range(1000)])
std=np.array([0 if rd.random()<0.5 else 1 for i in range(1000)])

print(auc(pre.copy(),std.copy()))
print(metrics.roc_auc_score(std,pre))

print(auc(pre.copy(),std.copy()))
print(metrics.roc_auc_score(std,pre))

print(auc(pre.copy(),std.copy()))
print(metrics.roc_auc_score(std,pre))

