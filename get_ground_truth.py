#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 weihao <blackhatdwh@gmail.com>
#
# Distributed under terms of the MIT license.
import pandas as pd

def read_ground_truth(file_name):
    answer = []
    f = open(file_name)
    while True:
        line = f.readline()
        if not line:
            break
        answer.append(line.rstrip('\n').split(',')[1])
    return answer

def get_result_for_classifier(file_name, which):
    answer = read_ground_truth(file_name)
    if which == 1:
        # if 'N' or 'O' --> 0
        # if 'A' or '~' --> 1
        d = list(map(lambda x: 0 if x in ['N', 'O'] else 1, answer))
        df = pd.DataFrame(data=d)
        return df.values.ravel()

    if which == 2:
        # if 'N' --> 0
        # if 'O' --> 1
        d = list(map(lambda x: 0 if x == 'N' else 1, answer))
        df = pd.DataFrame(data=d)
        return df

    if which == 3:
        # if 'A' --> 0
        # if '~' --> 1
        d = list(map(lambda x: 0 if x == 'A' else 1, answer))
        df = pd.DataFrame(data=d)
        return df
