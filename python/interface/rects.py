import numpy as np
from disque import *


def rect(centres,rayons):
    n = np.size(centres)
    max_r = centres[0].real+rayons[0]
    min_r = centres[0].real-rayons[0]
    max_i = centres[0].imag+rayons[0]
    min_i = centres[0].imag+rayons[0]
    for i in range (1,n):
        tmp1 = centres[i].real+rayons[i]
        tmp2 = centres[i].real-rayons[i]
        tmp3 = centres[i].imag+rayons[i]
        tmp4 = centres[i].imag-rayons[i]
        if(tmp1 > max_r):
            max_r = tmp1
        if(tmp2 < min_r):
            min_r = tmp2
        if(tmp3 > max_i):
            max_i = tmp3
        if(tmp4 < min_i):
            min_i = tmp4
    return max_r,min_r,max_i,min_i
