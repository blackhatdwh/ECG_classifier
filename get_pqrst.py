#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 weihao <blackhatdwh@gmail.com>
#
# Distributed under terms of the MIT license.

import numpy as np


def get_pqrst(out):
    filtered = out['filtered']
    Rpeaks = out['rpeaks']
    Qpeaks = np.ndarray(shape=[0])
    Speaks = np.ndarray(shape=[0])
    Ppeaks = np.ndarray(shape=[0])
    Tpeaks = np.ndarray(shape=[0])
    for Rpeak in Rpeaks:
        idx = Rpeak
        try:
            while filtered[idx] > filtered[idx+1]:
                idx += 1
            Speaks = np.append(Speaks, idx)
        except:
            pass
    
        idx = Rpeak
        try:
            while filtered[idx] > filtered[idx-1]:
                idx -= 1
            Qpeaks = np.append(Qpeaks, idx)
        except:
            pass
    

    for Speak in Speaks:
        idx = int(Speak)
        try:
            while filtered[idx] < filtered[idx+1] or filtered[idx] < filtered[idx+10]:
                idx += 1
            Tpeaks = np.append(Tpeaks, idx)
        except:
            pass

    
    for Qpeak in Qpeaks:
        idx = int(Qpeak)
        try:
            while filtered[idx] < filtered[idx-1] or filtered[idx] < filtered[idx-10]:
                idx -= 1
            Ppeaks = np.append(Ppeaks, idx)
        except:
            pass


    return [Ppeaks, Qpeaks, Rpeaks, Speaks, Tpeaks]
