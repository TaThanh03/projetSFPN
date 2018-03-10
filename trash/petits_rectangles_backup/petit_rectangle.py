import numpy as np
from disque import disque 

def petit_rectangle(A,eps):
    centres, rayons = disque(A, eps)
    n = np.size(centres)
    max_r = np.zeros(n)
    min_r = np.zeros(n)
    max_i = np.zeros(n)
    min_i = np.zeros(n)
    for i in range (n):
        tmp1 = centres[i].real + rayons[i]
        tmp2 = centres[i].real - rayons[i]
        tmp3 = centres[i].imag + rayons[i]
        tmp4 = centres[i].imag - rayons[i]
        max_r[i] = tmp1
        min_r[i] = tmp2
        max_i[i] = tmp3
        min_i[i] = tmp4
    return max_r, min_r, max_i, min_i