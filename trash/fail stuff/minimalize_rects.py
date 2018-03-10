#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
"""
import numpy as np
from rectangle_collision_check import rectangle_collision_check
from merge_rects import merge_rects

def minimalize_rects(max_r, min_r, max_i, min_i):
    X = list(min_r)
    Y = list(min_i)
    W = list(np.subtract(max_r, min_r))
    H = list(np.subtract(max_i, min_i))
    """
    print(X)
    print(Y)
    print(W)
    print(H)
    """
    merge_continue = 1
    
    while merge_continue == 1:
        n = len(X)
        collide_once = 0
        for i in range(0, n):
            for j in range(i+1, n):  
                collide, couvert = rectangle_collision_check(X[i],Y[i],W[i],H[i],X[j],Y[j],W[j],H[j])
                if collide == 1:
                    if couvert == 0:    
                        Xnew, Ynew, Wnew, Hnew = merge_rects(X[i],Y[i],W[i],H[i],X[j],Y[j],W[j],H[j])
                        print(Xnew, Ynew, Wnew, Hnew)
                        X.pop(j)
                        Y.pop(j)
                        W.pop(j)
                        H.pop(j)
                        X.pop(i)
                        Y.pop(i)
                        W.pop(i)
                        H.pop(i)
                        X.append(Xnew)
                        Y.append(Ynew)
                        W.append(Wnew)
                        H.append(Hnew)
                    if couvert == 1:
                        X.pop(j)
                        Y.pop(j)
                        W.pop(j)
                        H.pop(j)
                    if couvert == 2:
                        X.pop(i)
                        Y.pop(i)
                        W.pop(i)
                        H.pop(i)
                    collide_once = 1
                    """
                    print("===========", collide, couvert)
                    print(X)
                    print(Y)
                    print(W)
                    print(H)
                    """
                    break
            if collide_once == 1:
                break
            if i == n-1 and collide_once == 0:
                merge_continue = 0
    max_r_ret = np.add(X, W)
    min_r_ret = np.copy(X)
    max_i_ret = np.add(Y, H)
    min_i_ret = np.copy(Y)
    return max_r_ret, min_r_ret, max_i_ret, min_i_ret

def test():
    max_r = np.zeros(8)
    min_r = np.zeros(8)
    max_i = np.zeros(8)
    min_i = np.zeros(8)
    max_r[0] = 3
    min_r[0] = 1
    max_i[0] = 3
    min_i[0] = 1
    
    max_r[1] = 4
    min_r[1] = 2
    max_i[1] = 4
    min_i[1] = 2

    max_r[2] = 7
    min_r[2] = 2
    max_i[2] = 12
    min_i[2] = 7

    max_r[3] = 6
    min_r[3] = 4
    max_i[3] = 11
    min_i[3] = 9

    max_r[4] = 8
    min_r[4] = 5
    max_i[4] = 4
    min_i[4] = 1

    max_r[5] = 10
    min_r[5] = 7
    max_i[5] = 5
    min_i[5] = 2

    max_r[6] = 11
    min_r[6] = 9
    max_i[6] = 6
    min_i[6] = 3
    
    max_r[7] = 11
    min_r[7] = 9
    max_i[7] = 10
    min_i[7] = 8
    
    A, B, C, D = minimalize_rects(max_r, min_r, max_i, min_i)
    print(A)
    print(B)
    print(C)
    print(D)