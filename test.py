#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 weihao <blackhatdwh@gmail.com>
#
# Distributed under terms of the MIT license.

from sklearn.ensemble import AdaBoostClassifier
from sklearn.externals import joblib

# X: data; which: which classifier
def test(X, which):
    model = joblib.load('model-%s.pkl' % which)
    return model.predict(X)
