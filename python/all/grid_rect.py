import numpy as np
from rect import rectangle
#import matplotlib.patches as patches
#import matplotlib.pyplot as plt
import pymp
import time


def grid_rect(A,eps,m,max_r,min_r,max_i,min_i,mode):
    n,r = np.shape(A)
    x = np.linspace(min_r,max_r,m)
    y = np.linspace(min_i,max_i,m)
    if mode == 1: #sequentiel
        sigmin = np.zeros((m,m))
        for k in range(m):
            for j in range(m):
                u,s,v = np.linalg.svd(complex(x[k],y[j])*np.eye(n)-A)
                sigmin[j,k] = s[-1]
    else: #parallel
        sigmin = pymp.shared.array((m,m))
        with pymp.Parallel(4) as p:
            for k in p.range(m):
                for j in range(m):
                    u,s,v = np.linalg.svd(complex(x[k],y[j])*np.eye(n)-A)
                    sigmin[j,k] = s[-1]                
    #plt.contour(x,y,sigmin,[eps])
    #plt.show()
    return x,y,sigmin

def show_grid_rect(A, eps, m, mode):
    max_r,min_r,max_i,min_i = rectangle(A,eps)
    start = time.time()
    x,y,sigmin = grid_rect(A, eps, m, max_r,min_r,max_i,min_i, mode)
    end = time.time()
    my_time = end - start
    return x,y,sigmin,my_time

def show_grid_rect_zoom(A, eps, m, max_r,min_r,max_i,min_i, mode):
    start = time.time()
    x,y,sigmin = grid_rect(A, eps, m, max_r,min_r,max_i,min_i, mode)
    end = time.time()
    my_time = end - start
    return x,y,sigmin,my_time
    
    
