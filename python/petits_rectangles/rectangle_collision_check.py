#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
couvert = 0 not couvert each other 
couvert = 1 first one couvert second one 
couvert = 2 second one couvert first one
"""


def rectangle_collision_check(X1, Y1, W1, H1, X2, Y2, W2, H2):
    collide = 0
    couvert = 0 
    if (X1+W1<X2 or X2+W2<X1 or Y1+H1<Y2 or Y2+H2<Y1):
        return collide, couvert
    else:
        collide = 1
        if (X1<X2 and X1+W1>X2+W2 and Y1<Y2 and Y1+H1>Y2+H2):
            couvert = 1
        if (X2<X1 and X2+W2>X1+W1 and Y2<Y1 and Y2+H2>Y1+H1):
            couvert = 2
    return collide, couvert