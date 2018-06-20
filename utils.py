#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 weihao <blackhatdwh@gmail.com>
#
# Distributed under terms of the MIT license.

import collections
import numpy as np

def flatten(x):
    if isinstance(x, collections.Iterable):
        return [a for i in x for a in flatten(i)]
    else:
        return [x]

def find_extreme_points(data, type):
    extremes_val = []
    extremes_loc = []
    if type == 'max':
        for i in range(len(data)):
            if i != 0 and i != len(data) - 1:
                if data[i] > data[i-1] and data[i] > data[i+1]:
                    extremes_loc.append(i)
                    extremes_val.append(data[i])
            else:
                pass

    if type == 'min':
        for i in range(len(data)):
            if i != 0 and i != len(data) - 1:
                if data[i] < data[i-1] and data[i] < data[i+1]:
                    extremes_loc.append(i)
                    extremes_val.append(data[i])
            else:
                pass

    if type == 'all':
        for i in range(len(data)):
            if i != 0 and i != len(data) - 1:
                if data[i] > data[i-1] and data[i] > data[i+1] or data[i] < data[i-1] and data[i] < data[i+1]:
                    extremes_loc.append(i)
                    extremes_val.append(data[i])
            else:
                pass

    result = {'value': np.array(extremes_val), 'loc': np.array(extremes_loc)}
    return result
