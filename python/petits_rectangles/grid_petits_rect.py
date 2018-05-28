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
        for l in range(s):
            for k in p.range(m):
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
    
    for i in range(s):
        tmp1 = x[1+i*m:(i+1)*m];
        tmp2 = y[1+i*m:(i+1)*m];
        tmp3 = sigmin[1+i*m:(i+1)*m,1+i*m:(i+1)*m];
        plt.contour(tmp1,tmp2,tmp3,[eps])
    plt.show()
    
    return x,y,sigmin,s

def main():
    """
    print(np.linalg.eig(A))
    """
    A = np.array([[5,0,0,-1],[1,0,-100,1],[-1.5,1,-200,1],[-1,100,3,-3]])
    start = time.time()
    grid_petits_rect(A,0.3,500)
    end = time.time()
    print("time", end - start)
    
main()
