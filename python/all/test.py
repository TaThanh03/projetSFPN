import numpy as np
import time
from grid_par_comp import grid_par_comp
from grid_rect import show_grid_rect
import matplotlib.pyplot as plt
from proj_corr import proj_corr, proj_corr_zoom

def test(taille_max,nb_test):
    epss = 0.3
    m = 300
    time_seq = np.zeros(taille_max-2)
    time_para = np.zeros(taille_max-2)
    x = np.zeros(taille_max-2)
    my_time_seq = np.zeros(nb_test)
    my_time_para = np.zeros(nb_test)
    for i in range (2,taille_max) :
        x[i-2] = i
        for k in range(nb_test):
            A = np.random.random((i,i))+np.random.random((i,i))*1j
            start = time.time()
            
            proj_corr(A, epss, 10000, float(0.0001), 1)
            #show_grid_rect(A, epss, m, 1)  
            end = time.time()
            my_time_seq[k] = end - start
            print(my_time_seq[k])
            start = time.time()
            proj_corr(A, epss, 10000, float(0.0001), 2)
            #show_grid_rect(A, epss, m, 2) 
            end = time.time()
            my_time_para[k] = end - start
            print(my_time_para[k])
        time_seq[i-2] = np.mean(my_time_seq)
        time_para[i-2] = np.mean(my_time_para)
    plt.plot(x,time_seq,"r-o",label = "Sequentiel")
    plt.plot(x,time_para,"b-o",label = "Parallele")
    plt.xlabel("taille de la matrice")
    plt.ylabel("temps de calcul")
    
    
    plt.legend()
    plt.savefig('grid_par_comp.png', transparent=False, bbox_inches='tight')
    plt.show()
    return

#test(9,20)
test(10,10)
