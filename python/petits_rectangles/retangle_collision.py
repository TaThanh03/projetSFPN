#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 23:08:19 2018

@author: ta
"""

def rectangle_collision(ret1, ret2):
    intersect = False
    if (X1+W1<X2 or X2+W2<X1 or Y1+H1<Y2 or Y2+H2<Y1):
        return intersect
    else:
        intersect = True
    return intersect