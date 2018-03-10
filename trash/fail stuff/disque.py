import numpy as np

def disque(A,eps):
    n,r= np.shape(A)
    rayons = np.zeros(n)
    centres = np.zeros(n)
    for i in range (n):
        centres[i] = A[i,i]
        for j in range (n):
            if(i!=j):
                rayons[i] = rayons[i]+abs(A[i,j])
        rayons[i] = rayons[i]+np.sqrt(n)*eps
    return centres,rayons