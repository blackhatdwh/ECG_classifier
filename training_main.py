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
from get_ground_truth import get_result_for_classifier, get_file_name_for_classifier
from utils import *
from train import train
import pandas as pd
import sys


def train_classifier_1(data_used=300):
    data = []
    for i in range(1, data_used + 1):
        print(i)
        file_name = '../training2017/A%s.mat' % str(i).zfill(5)
        out = get_mat(file_name)
        ecg = out['filtered']
        P_index, Q_index, R_index, S_index, T_index = get_pqrst(out)
        features = get_features(ecg, P_index, Q_index, R_index, S_index, T_index)
        data.append(flatten(features))

    df = pd.DataFrame(data=data)
    target = get_result_for_classifier('../training2017/REFERENCE.csv', 1)
    train(df, target[:len(df)], 1)

def train_classifier_2(data_used=300):
    useful_file_names = get_file_name_for_classifier('../training2017/REFERENCE.csv', 2)
    data = []
    for i in range(1, data_used + 1):
        if i in useful_file_names:
            print(i)
            file_name = '../training2017/A%s.mat' % str(i).zfill(5)
            out = get_mat(file_name)
            ecg = out['filtered']
            P_index, Q_index, R_index, S_index, T_index = get_pqrst(out)
            features = get_features(ecg, P_index, Q_index, R_index, S_index, T_index)
            data.append(flatten(features))

    df = pd.DataFrame(data=data)
    target = get_result_for_classifier('../training2017/REFERENCE.csv', 2)
    train(df, target[:len(df)], 2)

def train_classifier_3(data_used=300):
    useful_file_names = get_file_name_for_classifier('../training2017/REFERENCE.csv', 3)
    data = []
    for i in range(1, data_used + 1):
        if i in useful_file_names:
            print(i)
            file_name = '../training2017/A%s.mat' % str(i).zfill(5)
            out = get_mat(file_name)
            ecg = out['filtered']
            P_index, Q_index, R_index, S_index, T_index = get_pqrst(out)
            features = get_features(ecg, P_index, Q_index, R_index, S_index, T_index)
            data.append(flatten(features))

    df = pd.DataFrame(data=data)
    target = get_result_for_classifier('../training2017/REFERENCE.csv', 3)
    train(df, target[:len(df)], 3)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 training_main.py 3000\nTraining from A00001.mat(include) to A3000.mat(include)')
        sys.exit(1)
    end_at = int(sys.argv[1])
    train_classifier_1(end_at)
    train_classifier_2(end_at)
    train_classifier_3(end_at)
