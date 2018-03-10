import numpy as np
from rectangle import rectangle
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import pymp
import time

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
    """
    sigmin = pymp.shared.array((m,m))
    n,r = np.shape(A)
    x = np.linspace(min_r,max_r,m)
    y = np.linspace(min_i,max_i,m)
    with pymp.Parallel(4) as p:
        for k in p.range(m):
            for j in range(m):
                u,s,v = np.linalg.svd(complex(x[k],y[j])*np.eye(n)-A)
                sigmin[j,k] = s[-1]
    """
    
    plt.figure()
    currentAxis = plt.gca()
    rect = patches.Rectangle((min_r,min_i),(max_r-min_r),(max_i-min_i),linewidth=1,edgecolor='r',facecolor='none')
    currentAxis.add_patch(rect)
    plt.contour(x,y,sigmin,[eps])
    plt.show()

def main():
    start = time.time() 
    """
    A = np.array([[1,2,3,4,5],[2,3,4,5,6],[5,6,4,3,7],[3,8,7,9,6],[1,2,3,6,7]])
    A = np.array([[5,0,0,-1],[1,0,-1,1],[-1.5,1,-2,1],[-1,1,3,-3]])
    A = np.array([[1,2],[1,-1]])
    A = np.array([[-0.558253,-0.0461681,-0.505735],[-0.411397,0.0365854,0.199707],[0.285389,-0.313789, 0.200189]])
    A = np.array([[1,0,-1,3,1,5],[-2,1,4,5,1,2],[1,8,7,4,9,4],[-7,6,-1,3,4,9],[-2,-4,3,4,2,5],[-6,1,2,5,6,7]])
    A = np.array([[1,0,4,-1,3,1,5],[-2,1,9,4,5,1,2],[1,8,7,1,4,9,4],[-2,-7,6,-1,3,4,9],[-2,-4,3,-8,4,2,5],[-6,1,-5,2,5,6,7],[-2,-4,-6,3,5,7,9]])
    A = np.array([[1,0,4,-1,3,4,1,5],[-2,-3,1,9,4,5,1,2],[1,8,-9,7,1,4,9,4],[-2,-7,5,6,-1,3,4,9],[-2,3,-4,3,-8,4,2,5],[-6,1,-5,2,-7,5,6,7],[-2,8,-4,-6,3,5,7,9],[3,4,6,7,-1,4,-3,8]])
    """
    A = np.array([[1,2,3,4,5],[2,3,4,5,6],[5,6,4,3,7],[3,8,7,9,6],[1,2,3,6,7]])
    grid_rect(A,0.3,1000)
    end = time.time()
    print("time", end - start)

main()