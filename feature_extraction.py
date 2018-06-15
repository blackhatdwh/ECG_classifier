#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 weihao <blackhatdwh@gmail.com>
#
# Distributed under terms of the MIT license.
from math import sqrt, pow
from scipy.stats import skew, kurtosis
from numpy import *

def get_simple_RR_features(RR):
    mean_RR = RR.mean()
    median_RR = median(RR)
    min_RR = RR.min()
    max_RR = RR.max()
    sk_RR = skew(RR)
    kurt_RR = kurtosis(RR)
    range_RR = max_RR - min_RR
    var_RR = var(RR)
    return [mean_RR, median_RR, min_RR, max_RR, sk_RR, kurt_RR, range_RR, var_RR]

def get_HRV_features(RR):
    diff_RR = diff(RR)
    RMSSD = sqrt((power(diff_RR, 2)).mean())
    SDSD = std(diff_RR)
    NN50 = len(list(filter(lambda x: abs(x) > 0.5, diff_RR)))
    pNN50 = NN50 / len(RR)
    NN20 = len(list(filter(lambda x: abs(x) > 0.2, diff_RR)))
    pNN20 = NN20 / len(RR)
    return [pNN20, pNN50, SDSD]

def get_poincare_feature(RR):
    x = RR[0:len(RR)-1]
    y = RR[1:len(RR)]
    L = len(RR)
    sumval = 0
    for i in range(L-2):
        sumval = sumval + sqrt(pow((x[i] - y[i]), 2) + pow((x[i+1] - y[i+1]), 2))
    sumval = sumval / (L-2)
    stepping = sumval / RR.mean()

    cp = (-1.0*RR[L-3]-RR[L-1]+2*sum(RR[:L-1])) / (2*(L-1))

    term1 = 0
    for i in range(L-1):
        term1 += pow((RR[i]-RR[i+1]), 2)
    term1 = term1 / (2*(L-1))

    term2 = 0
    for i in range(L-1):
        term2 = term2 + abs(RR[i]-RR[i+1])
    term2 = term2 / (sqrt(2)*(L-1))
    term2 = pow(term2, 2)

    dispersion = sqrt(term1-term2) / cp
    return [stepping, dispersion]
