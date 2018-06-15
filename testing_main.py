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

if __name__ == '__main__':
    #testing_sample = sys.argv[1]
    predict = []
    for i in range(1000, 2000):
        print(i)
        file_name = '../training2017/A%s.mat' % str(i).zfill(5)
        out = get_mat(file_name)
        ecg = out['filtered']
        P_index, Q_index, R_index, S_index, T_index = get_pqrst(out)
        features = get_features(ecg, P_index, Q_index, R_index, S_index, T_index)
        data = flatten(features)

        df = pd.DataFrame(data=data).transpose()

        predict.append(test(df))


    target = get_result_for_classifier('../training2017/REFERENCE.csv', 1)
    target = target[999:1999]


    true = 0
    for i in range(1000):
        if predict[i] == target[i]:
            true += 1

    print(true/1000)

