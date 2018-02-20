# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

def disque2(A, eps):
    n = len(A)
    rayons = np.zeros((1,n)) 
    centre = np.zeros(n)
    for i in range(1, n):
         centre.itemset(i, A.item((i,i)))
         for j in range(1, n):
             if not i == j:
                 tmp = rayons.item(i) + np.absolute(A.item((i, j))) + eps
                 rayons.itemset(i, tmp)   
    return centre, rayons

def rectangle2(A,eps):
    centre, rayons = disque2(A, eps)
    max_r = 0
    min_r = 0  
    max_i = 0
    min_i = 0
    for i in range(1, centre.size):
        tmp1 = np.real(centre.item(i)) + rayons.item(i)
        tmp2 = np.imag(centre.item(i)) + rayons.item(i)
        if tmp1 > max_r:
            max_r = tmp1
        if(tmp1 < min_r):
            min_r = tmp1
        if(tmp2 > max_i):
            max_i = tmp2
        if(tmp2 < min_i):
            min_i = tmp2
    return max_r, min_r, max_i, min_i

def grid_rect2(A,epss,m):
    sigmin = np.zeros(shape=(m, m))
    x = []
    y = []
    max_r,min_r,max_i,min_i = rectangle2(A,epss)
    print(max_r,min_r,max_i,min_i)
    n = len(A)
    id_n = np.identity(n)
    x = np.linspace(min_r, max_r, m)
    y = np.linspace(min_i, max_i, m)
    for k in range(1, m):
        for j in range(1, m):
            tmp =   np.subtract( np.dot(x[k]+y[j]*1j, id_n),  A )
            u, s, vh = np.linalg.svd(tmp, full_matrices=True)
            a = min(s)
            sigmin.itemset((j,k), a)
    """
    plt.imshow(sigmin)
    plt.show()
    """
    plt.plot(sigmin, 'ro')
    plt.axis([-4, 20, -4, 10])
    plt.show()
    
def main():
    A = np.matrix('5 0 0 -1; 1 0 -1 1; -1.5 1 -2 1; -1 1 3 -3')
    epss = 0.2
    m = 10
    grid_rect2(A,epss,m)
    
main()

    
    

