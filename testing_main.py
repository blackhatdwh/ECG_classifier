#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 weihao <blackhatdwh@gmail.com>
#
# Distributed under terms of the MIT license.

from get_mat import get_mat
from get_pqrst import get_pqrst
from get_features import get_features
from get_ground_truth import get_result_for_classifier
from utils import *
from test import test
import pandas as pd
import sys


if len(sys.argv) != 3:
    print('Usage: python3 testing_main.py 1000 3000\nTesting from A01000.mat(include) to A03000.mat(exclude)')

start_from = int(sys.argv[1])
end_at = int(sys.argv[2])
testing_length = end_at - start_from

predict = []
for i in range(start_from, end_at):
    file_name = '../training2017/A%s.mat' % str(i).zfill(5)
    out = get_mat(file_name)
    ecg = out['filtered']
    P_index, Q_index, R_index, S_index, T_index = get_pqrst(out)
    features = get_features(ecg, P_index, Q_index, R_index, S_index, T_index)
    data = flatten(features)

    df = pd.DataFrame(data=data).transpose()

    # classifier 1
    layer_1_result = test(df, 1)
    
    # classifier 2
    # N-->0, O-->2
    if layer_1_result == 0:
        layer_2_result = test(df, 2)
        predict.append(0 if layer_2_result == 0 else 2)
    # A-->1, ~-->3
    else:
        layer_2_result = test(df, 3)
        predict.append(1 if layer_2_result == 0 else 3)


target = get_result_for_classifier('../training2017/REFERENCE.csv', 4)
target = target[start_from-1:end_at-1]

result = [[0 for i in range(4)] for j in range(4)]

for i in range(testing_length):
    result[predict[i]][target[i]] += 1


sigma_n = 0
sigma_a = 0
sigma_o = 0
sigma_p = 0
sigma_N = 0
sigma_A = 0
sigma_O = 0
sigma_P = 0
for i in range(4):
    sigma_n += result[i][0]
    sigma_a += result[i][1]
    sigma_o += result[i][2]
    sigma_p += result[i][3]
    sigma_N += result[0][i]
    sigma_A += result[1][i]
    sigma_O += result[2][i]
    sigma_P += result[3][i]

F_1n = 2 * result[0][0] / (sigma_N + sigma_n)
F_1a = 2 * result[1][1] / (sigma_A + sigma_a)
F_1o = 2 * result[2][2] / (sigma_O + sigma_o)
F_1p = 2 * result[3][3] / (sigma_P + sigma_p)

F_1 = (F_1n + F_1a + F_1o + F_1p) / 4

print('table')
for i in range(4):
        print(result[i][0] + '\t' + result[i][1] + '\t' +result[i][2] + '\t' +result[i][3] + '\t')

print('\n')
print("F1: ", F_1)
