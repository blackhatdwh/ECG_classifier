#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 weihao <blackhatdwh@gmail.com>
#
# Distributed under terms of the MIT license.

from numpy import *
from math import sqrt
from feature_extraction import *

def get_features(ecg_data, Ppeaks, Qpeaks, Rpeaks, Speaks, Tpeaks):
    features = []

    RR = diff(Rpeaks)

    features.append(get_simple_RR_features(RR))
    features.append(get_HRV_features(RR))
    features.append(get_poincare_feature(RR))

    return features

