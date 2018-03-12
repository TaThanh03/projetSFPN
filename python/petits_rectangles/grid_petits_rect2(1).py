import numpy as np
from petits_rect import *
import matplotlib.pyplot as plt

def grid_petits_rect(A,eps,m):
    (max_r,min_r,max_i,min_i) = petits_rect(A,eps)
    s = np.size(max_r)
    sigmin = np.zeros((m*s,m*s))
    n,r = np.shape(A)
    x = np.zeros(s*m)
    y = np.zeros(s*m)
    
    for l in range (s):
        tmp1 = np.linspace(min_r[l],max_r[l],m)
        tmp2 = np.linspace(min_i[l],max_i[l],m)
        for k in range(m):
            x[(l-1)*m+k] = tmp1[k]
            y[(l-1)*m+k] = tmp2[k]
    
    for l in range(s):
        for k in range(m):
            for j in range(m):
                u,s1,v = np.linalg.svd(complex(x[k+(l-1)*m],y[j+(l-1)*m])*np.eye(n)-A)
                sigmin[j+l*m,k+l*m] = s1[-1]
                
                
    for i in range(s):
        tmp1 = x[1+i*m:(i+1)*m];
        tmp2 = y[1+i*m:(i+1)*m];
        tmp3 = sigmin[1+i*m:(i+1)*m,1+i*m:(i+1)*m];
        plt.contour(tmp1,tmp2,tmp3,[eps])

    plt.show()


A = np.array([[1,0,0,0,0],[2,10,0,0,1],[2,2,70,0,8],[2,4,1,2,6],[2,1,1,1,20]])
print(np.linalg.eig(A))
grid_petits_rect(A,0.3,100)