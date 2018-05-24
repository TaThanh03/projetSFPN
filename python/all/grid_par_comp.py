import numpy as np
from rect import rectangle
#import matplotlib.pyplot as plt
import time
import pymp

def grid_par_comp(A, eps, m, mode):
    (max_r,min_r,max_i,min_i) = rectangle(A,eps)
    n,r = np.shape(A)
    E = np.ones((n,n))
    x = np.linspace(min_r,max_r,m)
    y = np.linspace(min_i,max_i,m)
    start = time.time()
    
    
    if mode == 1:
        p = np.zeros((m,m))
        for k in range(m):
            for j in range(m):
                X = abs(np.linalg.inv(A - ((x[k]+y[j]*1j)*np.eye(n))));
                Y = np.dot(X,E);
                s,v = np.linalg.eig(Y)
                p[j,k] = max(abs(s));     
    else:
        p = pymp.shared.array((m,m))
        with pymp.Parallel(4) as pimp:
            for k in pimp.range(m):
                for j in range(m):
                    X = abs(np.linalg.inv(A - ((x[k]+y[j]*1j)*np.eye(n))));
                    Y = np.dot(X,E);
                    s,v = np.linalg.eig(Y)
                    p[j,k] = max(abs(s))
            
    """
    plt.contour(x,y,p,[eps])
    plt.show()
    """
    end = time.time()
    mytime = end -start
    return x,y,p,mytime


#A = np.array([[1,1,1,1],[2,60,2,2],[1,1,20,1],[1,2,5,20j]])
#epss = 0.3
#m = 100
#grid_par_comp(A,1./epss,m)

