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

def get_file_name_for_classifier(file_name, which):
    answer = read_ground_truth(file_name)
    if which == 2:
        return [i + 1 for i, x in enumerate(answer) if x == 'N' or x == 'O']
    if which == 3:
        return [i + 1 for i, x in enumerate(answer) if x == 'A' or x == '~']

def get_result_for_classifier(file_name, which):
    answer = read_ground_truth(file_name)
    # classifier 1
    if which == 1:
        # if 'N' or 'O' --> 0
        # if 'A' or '~' --> 1
        d = list(map(lambda x: 0 if x in ['N', 'O'] else 1, answer))
        df = pd.DataFrame(data=d)
        return df.values.ravel()

    # classifier 2
    if which == 2:
        # if 'N' --> 0
        # if 'O' --> 1
        answer = filter(lambda x: x == 'N' or x == 'O', answer)
        d = list(map(lambda x: 0 if x == 'N' else 1, answer))
        df = pd.DataFrame(data=d)
        return df.values.ravel()

    # classifier 3
    if which == 3:
        # if 'A' --> 0
        # if '~' --> 1
        answer = filter(lambda x: x == 'A' or x == '~', answer)
        d = list(map(lambda x: 0 if x == 'A' else 1, answer))
        df = pd.DataFrame(data=d)
        return df.values.ravel()

    # calculate accuracy
    if which == 4:
        # if 'N' --> 0
        # if 'A' --> 1
        # if 'O' --> 2
        # if '~' --> 3
        d = list(map(lambda x: ['N', 'A', 'O', '~'].index(x), answer))
        df = pd.DataFrame(data=d)
        return df.values.ravel()
