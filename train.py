#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 weihao <blackhatdwh@gmail.com>
#
# Distributed under terms of the MIT license.

from sklearn import model_selection
from sklearn.ensemble import AdaBoostClassifier
from sklearn.externals import joblib
def train(X, Y):
    model = AdaBoostClassifier(n_estimators=30, random_state=7)
    model.fit(X, Y)
    joblib.dump(model, 'model.pkl')
