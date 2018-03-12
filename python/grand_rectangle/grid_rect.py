import numpy as np
from rectangle import rectangle
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import pymp
import time

def grid_rect(A,eps,m):
    (max_r,min_r,max_i,min_i) = rectangle(A,eps)
    """
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
    """
    print("size", n, "m", m)
    plt.contour(x,y,sigmin,[eps])
    plt.show()

def main():
    A = np.array([[1,20],[-10,-1]])
    
    start = time.time()
    grid_rect(A,0.3,1000)
    end = time.time()
    print("time", end - start)
    
    A = np.array([[-0.558253,-0.0461681,-0.505735],[-0.411397,0.0365854,0.199707],[0.285389,-0.313789, 0.200189]])
    
    start = time.time()
    grid_rect(A,0.3,1000)
    end = time.time()
    print("time", end - start)
    
    A = np.array([[5,0,0,-1],[1,0,-100,1],[-1.5,1,-200,1],[-1,100,3,-3]])
    
    start = time.time()
    grid_rect(A,0.3,1000)
    end = time.time()
    print("time", end - start)
    
    A = np.array([[1,0,0,0,0],[2,10,0,0,1],[2,2,70,0,8],[2,4,1,2,6],[2,1,1,1,20]])
    
    start = time.time()
    grid_rect(A,0.3,1000)
    end = time.time()
    print("time", end - start)
    
    A = np.array([[1,0,-1,3,1,5],[-2,100,4,5,1,2],[1,8,7,4,9,4],[-7,6,-1,3,4,9],[-2,-4,3,1,2,5],[-6,1,2,5,6,70]])
    
    start = time.time()
    grid_rect(A,0.3,1000)
    end = time.time()
    print("time", end - start)
    
    A = np.array([[1,0,4,-1,3,1,5],[-2,100,9,400,5,1,2],[1,8,7,1,4,9,4],[-2,-7,6,-100,3,4,9],[-2,-1,3,-8,4,2,5],[-6,100,-5,2,5,6,7],[-2,-4,-6,3,5,7,900]])
    
    
    start = time.time()
    grid_rect(A,0.3,1000)
    end = time.time()
    print("time", end - start)
    
    A = np.array([[1,0,144,-1,3,4,1,5],[-100,-3,1,100,4,5,1,2],[8,8,-9,87,1,4,9,4],[-2,-57,5,6,-100,35,4,9],[-2,3,-4,3,-8,57,2,5],[-7,1,-5,7,-7,500,5,7],[-2,8,-4,-6,3,100,7,9],[3,4,6,8,-100,4,-3,89]])
    
    start = time.time()
    grid_rect(A,0.3,1000)
    end = time.time()
    print("time", end - start)
    
main()