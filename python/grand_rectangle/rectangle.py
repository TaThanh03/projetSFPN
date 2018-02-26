import numpy as np
from disque import disque 
import matplotlib.pyplot as plt

def rectangle(A,eps):
    centres,rayons = disque(A,eps)
    n = np.size(centres)
    max_r = 0
    min_r = 0
    max_i = 0
    min_i = 0
    for i in range (n):
        tmp1 = centres[i].real + rayons[i]
        tmp2 = centres[i].real - rayons[i]
        tmp3 = centres[i].imag + rayons[i]
        tmp4 = centres[i].imag - rayons[i]
        if(tmp1 > max_r):
            max_r = tmp1
        if(tmp2 < min_r):
            min_r = tmp2
        if(tmp3 > max_i):
            max_i = tmp3
        if(tmp4 < min_i):
            min_i = tmp4

    
    fig, ax = plt.subplots()
    for i in range (n):
        circle = plt.Circle((centres[i].real, centres[i].imag), rayons[i], color='b', fill=False)
        ax.add_artist(circle)
    ax.set_xlim((min_r, max_r))
    ax.set_ylim((min_i, max_i))
    fig.show()
    
    return max_r,min_r,max_i,min_i