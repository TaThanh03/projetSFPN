import numpy as np
from petits_rect import petits_rect
import matplotlib.pyplot as plt
import pymp
import time

def grid_petits_rect(A,eps,m):
    (max_r,min_r,max_i,min_i,max_r_grand_rect,min_r_grand_rect,max_i_grand_rect,min_i_grand_rect) = petits_rect(A,eps)
    """
    sigmin = pymp.shared.array((m,m))
    n,r = np.shape(A)
    s = np.size(max_r)
    print("S", s)
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
                    sigmin[j+(l-1)*m,k+(l-1)*m] = s1[-1]
                    
    """
    n,r = np.shape(A)
    s = np.size(max_r)
    print("S", s)
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
                sigmin[j+(l-1)*m,k+(l-1)*m] = s1[-1]
    
    
    for i in range(s):
        tmp1 = x[1+i*m:(i+1)*m];
        tmp2 = y[1+i*m:(i+1)*m];
        tmp3 = sigmin[1+i*m:(i+1)*m,1+i*m:(i+1)*m];
        plt.contour(tmp1,tmp2,tmp3,[eps])
    plt.show()

def main():
    """
    A = np.array([[1,2,3,4,5],[2,3,4,5,6],[5,6,4,3,7],[3,8,7,9,6],[1,2,3,6,7]])
    A = np.array([[5,0,0,-1],[1,0,-1,1],[-1.5,1,-2,1],[-1,1,3,-3]])
    A = np.array([[1,2],[1,-1]])
    A = np.array([[-0.558253,-0.0461681,-0.505735],[-0.411397,0.0365854,0.199707],[0.285389,-0.313789, 0.200189]])
    A = np.array([[1,0,-1,3,1,5],[-2,1,4,5,1,2],[1,8,7,4,9,4],[-7,6,-1,3,4,9],[-2,-4,3,4,2,5],[-6,1,2,5,6,7]])
    A = np.array([[1,0,4,-1,3,1,5],[-2,1,9,4,5,1,2],[1,8,7,1,4,9,4],[-2,-7,6,-1,3,4,9],[-2,-4,3,-8,4,2,5],[-6,1,-5,2,5,6,7],[-2,-4,-6,3,5,7,9]])
    A = np.array([[1,0,4,-1,3,4,1,5],[-2,-3,1,9,4,5,1,2],[1,8,-9,7,1,4,9,4],[-2,-7,5,6,-1,3,4,9],[-2,3,-4,3,-8,4,2,5],[-6,1,-5,2,-7,5,6,7],[-2,8,-4,-6,3,5,7,9],[3,4,6,7,-1,4,-3,8]])
    A = np.array([[1,0,4444,-1,3467,444,1,5],[-100,-3,1,900,4,5,1,2],[1578,8,-9,5787,1,4,9,4],[-2,-57577,5,6,-1,3575,4,9],[-2,3478,-444,3,-8,574,2,5],[-6547,1,-5,2577,-7,5,556,7],[-2,8,-488,-6,3,5789,7,9],[3778,4,6,7788,-1,4,-3,87989]])
    print(np.linalg.eig(A))
    """ 
    start = time.time()
    A = np.array([[1,0,4444,-1,3467,444,1,5],[-100,-3,1,900,4,5,1,2],[1578,8,-9,5787,1,4,9,4],[-2,-57577,5,6,-1,3575,4,9],[-2,3478,-444,3,-8,574,2,5],[-6547,1,-5,2577,-7,5,556,7],[-2,8,-488,-6,3,5789,7,9],[3778,4,6,7788,-1,4,-3,87989]])
    grid_petits_rect(A,0.3,200)
    end = time.time()
    print("time", end - start)
    
main()