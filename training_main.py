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
from train import train
import pandas as pd

if __name__ == '__main__':
    data_used = 1000
    data = []
    #for i in range(1, 8529):
    for i in range(1, data_used):
        print(i)
        file_name = '../training2017/A%s.mat' % str(i).zfill(5)
        out = get_mat(file_name)
        ecg = out['filtered']
        P_index, Q_index, R_index, S_index, T_index = get_pqrst(out)
        features = get_features(ecg, P_index, Q_index, R_index, S_index, T_index)
        data.append(flatten(features))

    df = pd.DataFrame(data=data)
    target = get_result_for_classifier('../training2017/REFERENCE.csv', 1)
    train(df, target[:data_used-1])
