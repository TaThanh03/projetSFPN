import numpy as np
from petits_rect import petits_rect
import matplotlib.pyplot as plt
import pymp
import time

def grid_petits_rect(A,eps,m):
    (max_r,min_r,max_i,min_i,m_scalar) = petits_rect(A,eps)
    m *= m_scalar
    m = int(m)
    
    n,r = np.shape(A)
    s = np.size(max_r)
    sigmin = pymp.shared.array((s*m,s*m))
    x = np.zeros(s*m)
    y = np.zeros(s*m)
    for l in range (s):
        tmp1 = np.linspace(min_r[l],max_r[l],m);
        tmp2 = np.linspace(min_i[l],max_i[l],m);
        for k in range(m):
            x[(l-1)*m+k] = tmp1[k];
            y[(l-1)*m+k] = tmp2[k];
    with pymp.Parallel(4) as p:
        for l in p.range(s):
            for k in range(m):
                for j in range(m):
                    u,s1,v = np.linalg.svd(complex(x[k+(l-1)*m],y[j+(l-1)*m])*np.eye(n)-A)
                    sigmin[j+l*m,k+l*m] = s1[-1]
                    
    """
    n,r = np.shape(A)
    s = np.size(max_r)
    sigmin = np.zeros((s*m,s*m))
    x = np.zeros(s*m)
    y = np.zeros(s*m)
    for l in range (s):
        tmp1 = np.linspace(min_r[l],max_r[l],m);
        tmp2 = np.linspace(min_i[l],max_i[l],m);
        for k in range(m):
            x[(l-1)*m+k] = tmp1[k];
            y[(l-1)*m+k] = tmp2[k];
    for l in range(s):
        for k in range(m):
            for j in range(m):
                u,s1,v = np.linalg.svd(complex(x[k+(l-1)*m],y[j+(l-1)*m])*np.eye(n)-A)
                sigmin[j+l*m,k+l*m] = s1[-1]
    """
    
    
    print("size", n, "S", s, "m", m)
    for i in range(s):
        tmp1 = x[1+i*m:(i+1)*m];
        tmp2 = y[1+i*m:(i+1)*m];
        tmp3 = sigmin[1+i*m:(i+1)*m,1+i*m:(i+1)*m];
        plt.contour(tmp1,tmp2,tmp3,[eps])
    plt.show()

def main():
    """
    print(np.linalg.eig(A))
    """
    A = np.array([[1,20],[-10,-1]])
    
    start = time.time()
    grid_petits_rect(A,0.3,1000)
    end = time.time()
    print("time", end - start)
    
    A = np.array([[-0.558253,-0.0461681,-0.505735],[-0.411397,0.0365854,0.199707],[0.285389,-0.313789, 0.200189]])
    
    start = time.time()
    grid_petits_rect(A,0.3,1000)
    end = time.time()
    print("time", end - start)
    
    A = np.array([[5,0,0,-1],[1,0,-100,1],[-1.5,1,-200,1],[-1,100,3,-3]])
    
    start = time.time()
    grid_petits_rect(A,0.3,1000)
    end = time.time()
    print("time", end - start)
    
    A = np.array([[1,0,0,0,0],[2,10,0,0,1],[2,2,70,0,8],[2,4,1,2,6],[2,1,1,1,20]])
    
    start = time.time()
    grid_petits_rect(A,0.3,1000)
    end = time.time()
    print("time", end - start)
    
    A = np.array([[1,0,-1,3,1,5],[-2,100,4,5,1,2],[1,8,7,4,9,4],[-7,6,-1,3,4,9],[-2,-4,3,1,2,5],[-6,1,2,5,6,70]])
    
    start = time.time()
    grid_petits_rect(A,0.3,1000)
    end = time.time()
    print("time", end - start)
    
    A = np.array([[1,0,4,-1,3,1,5],[-2,100,9,400,5,1,2],[1,8,7,1,4,9,4],[-2,-7,6,-100,3,4,9],[-2,-1,3,-8,4,2,5],[-6,100,-5,2,5,6,7],[-2,-4,-6,3,5,7,900]])
    
    start = time.time()
    grid_petits_rect(A,0.3,1000)
    end = time.time()
    print("time", end - start)
    
    A = np.array([[1,0,144,-1,3,4,1,5],[-100,-3,1,100,4,5,1,2],[8,8,-9,87,1,4,9,4],[-2,-57,5,6,-100,35,4,9],[-2,3,-4,3,-8,57,2,5],[-7,1,-5,7,-7,500,5,7],[-2,8,-4,-6,3,100,7,9],[3,4,6,8,-100,4,-3,89]])
    
    start = time.time()
    grid_petits_rect(A,0.3,1000)
    end = time.time()
    print("time", end - start)
    
    
main()