import numpy as np
from rectangle import rectangle
import matplotlib.patches as patches
import matplotlib.pyplot as plt

def grid_rect(A,eps,m):
    (max_r,min_r,max_i,min_i) = rectangle(A,eps)
    sigmin = np.zeros((m,m))
    n,r = np.shape(A)
    x = np.linspace(min_r,max_r,m)
    y = np.linspace(min_i,max_i,m)
    for k in range(m):
        for j in range(m):
            u,s,v = np.linalg.svd(complex(x[k],y[j])*np.eye(n)-A)
            sigmin[j,k] = s[-1]
    plt.figure()
    currentAxis = plt.gca()
    rect = patches.Rectangle((min_r,min_i),(max_r-min_r),(max_i-min_i),linewidth=1,edgecolor='r',facecolor='none')
    currentAxis.add_patch(rect)
    plt.contour(x,y,sigmin,[eps])
    plt.show()


A = np.array([[1,2,3,4,5],[2,3,4,5,6],[5,6,4,3,7],[3,8,7,9,6],[1,2,3,6,7]])
grid_rect(A,0.3,1000)
"""
A = np.array([[5,0,0,-1],[1,0,-1,1],[-1.5,1,-2,1],[-1,1,3,-3]])
grid_rect(A,0.3,200)
"""