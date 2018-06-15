#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 weihao <blackhatdwh@gmail.com>
#
# Distributed under terms of the MIT license.

import matplotlib.pyplot as plt

def get_all_peak_value(ecg):
    peaks = []
    for i in range(len(ecg)-1):
        if i == 0:
            pass
        if ecg[i] > ecg[i-1] and ecg[i] > ecg[i+1]:
            peaks.append(ecg[i])
        if ecg[i] < ecg[i-1] and ecg[i] < ecg[i+1]:
            peaks.append(ecg[i])
    return peaks


def check_if_inverted(ecg):
    peaks = get_all_peak_value(ecg)
    highest = sorted(peaks, reverse=True)[:10]
    lowest = sorted(peaks)[:10]
    highest_avg = sum(highest) / len(highest)
    lowest_avg = sum(lowest) / len(lowest)
    total_avg = sum(ecg) / len(ecg)
    if (highest_avg - total_avg) < (total_avg - lowest_avg):
        return True
    else:
        return False
