import numpy as np
from rectangle import *
import matplotlib.pyplot as plt

def grid_par_comp(A,eps,m,E):
    (max_r,min_r,max_i,min_i) = rectangle(A,eps)
    p = np.zeros((m,m))
    n,r = np.shape(A)
    x = np.linspace(min_r,max_r,m)
    y = np.linspace(min_i,max_i,m)
    for k in range(m):
        for j in range(m):
            #1
            X = abs(np.linalg.inv(A - ((x[k]+y[j]*1j)*np.eye(n))));
            #2
            Y = np.dot(X,E);
            #3
            s,v = np.linalg.eig(Y)
            p[j,k] = max(abs(s));
    plt.contour(x,y,p,[eps])#1/eps
    plt.show()


A = np.array([[1,1,1,1],[2,60,2,2],[1,1,20,1],[1,2,5,20j]])
E = np.eye(4) #matrice des "1"
grid_par_comp(A,1,100,E)

#interface
#- choix de algo
#- avancer le raport
#- temps calcul

#- apliquer prediction correction sur sur "grid_par_comp"

