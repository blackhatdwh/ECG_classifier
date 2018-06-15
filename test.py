#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 weihao <blackhatdwh@gmail.com>
#
# Distributed under terms of the MIT license.

from sklearn.ensemble import AdaBoostClassifier
from sklearn.externals import joblib

def test(X):
    model = joblib.load('model.pkl')
    return model.predict(X)
