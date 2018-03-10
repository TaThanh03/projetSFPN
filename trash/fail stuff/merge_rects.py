#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
"""

def merge_rects(X1, Y1, W1, H1, X2, Y2, W2, H2):
    X = min(X1, X2)
    Y = min(Y1, Y2)
    W = max(X1+W1, X2+W2) - min(X1, X2)
    H = max(Y1+H1, Y2+H2) - min(Y1, Y2)
    return X, Y, W, H
