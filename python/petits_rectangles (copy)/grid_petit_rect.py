import numpy as np
from petit_rectangle import petit_rectangle
import matplotlib.patches as patches
import matplotlib.pyplot as plt

def grid_petit_rect(A,eps,m):
    (max_r,min_r,max_i,min_i) = petit_rectangle(A,eps)
    n,r = np.shape(A)
    sigmin = np.zeros((m + n*m, m + n*m))
    x = np.zeros(n*m)
    y = np.zeros(n*m)
    for l in range(n):
        tmp1 = np.linspace(min_r[l],max_r[l],m)
        tmp2 = np.linspace(min_i[l],max_i[l],m)
        for k in range(m):
            x[(l-1)*m+k] = tmp1[k]
            y[(l-1)*m+k] = tmp2[k]
    for l in range(n):
        for k in range(m):
            for j in range(m):
                u,s,v = np.linalg.svd(complex(x[(l-1)*m+k],y[(l-1)*m+j])*np.eye(n)-A)
                sigmin[j+(l-1)*m, k+(l-1)*m] = s[-1]
    for i in range(n):
        tmp1 = x[1+(i-1)*m:i*m]
        tmp2 = y[1+(i-1)*m:i*m]
        tmp3 = sigmin[ 1+(i-1)*m : i*m , 1+(i-1)*m : i*m ]    
        if len(tmp3) >= 0:
            plt.contour(tmp1, tmp2, tmp3, [eps])
    """
    plt.figure()
    currentAxis = plt.gca()
    rect = patches.Rectangle((min_r,min_i),(max_r-min_r),(max_i-min_i),linewidth=1,edgecolor='r',facecolor='none')
    currentAxis.add_patch(rect)
    """
    plt.show()


A = np.array([[1,2,3,4,5],[2,3,4,5,6],[5,6,4,3,7],[3,8,7,9,6],[1,2,3,6,7]])
grid_petit_rect(A,0.3,500)
"""
A = np.array([[5,0,0,-1],[1,0,-1,1],[-1.5,1,-2,1],[-1,1,3,-3]])
grid_petit_rect(A,0.3,100)
"""