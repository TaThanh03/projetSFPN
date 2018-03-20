import numpy as np
from disque import disque 
from minimalize_rects import minimalize_rects 
import matplotlib.pyplot as plt

def petit_rectangle(A,eps):
    centres, rayons = disque(A, eps)
    n = np.size(centres)
    most_max_r = 0
    most_min_r = 0
    most_max_i = 0
    most_min_i = 0
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
        if(tmp1 > most_max_r):
            most_max_r = tmp1
        if(tmp2 < most_min_r):
            most_min_r = tmp2
        if(tmp3 > most_max_i):
            most_max_i = tmp3
        if(tmp4 < most_min_i):
            most_min_i = tmp4
    fig, ax = plt.subplots()
    for i in range (n):
        circle = plt.Circle((centres[i].real, centres[i].imag), rayons[i], color='b', fill=False)
        ax.add_artist(circle)
    ax.set_xlim((most_min_r, most_max_r))
    ax.set_ylim((most_min_i, most_max_i))
    fig.show()
    max_r_op, min_r_op, max_i_op, min_i_op = minimalize_rects(max_r, min_r, max_i, min_i)
    return max_r_op, min_r_op, max_i_op, min_i_op