#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 weihao <blackhatdwh@gmail.com>
#
# Distributed under terms of the MIT license.


import scipy.io.matlab as matlab
import matplotlib.pyplot as plt
import numpy as np
from biosppy.signals import ecg
from check_invert import check_if_inverted

# 'which' indicates which mat to load
def get_mat(file_name):
    arr = matlab.loadmat(file_name)['val'][0]
    # if inverted, invert.
    if check_if_inverted(arr):
        arr = np.negative(arr)
    # use biosppy to filter and get R peaks
    out = ecg.ecg(signal=arr, sampling_rate=300., show=False)
    return out
