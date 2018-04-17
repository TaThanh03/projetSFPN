import numpy as np
from disque import disque
from rects import rect
def petits_rect(A,eps):
    centres,rayons = disque(A,eps)
    n,r = np.shape(A)
    centre2 = []
    rayons2 = []
    tmp2 = []
    max_r = []
    min_r = []
    max_i = []
    min_i = []
    liste = np.zeros((n,n))
    tmp = np.zeros((n,n))
    for i in range (n):
        for j in range (i,n):
            dist = np.sqrt((((centres[i].real)-(centres[j].real))**2)+((centres[i].imag)-(centres[j].imag))**2)
            if(dist<rayons[i]+rayons[j]):
                liste[i,j] = 1
                liste[j,i] = 1
    while((tmp!=liste).any()):
        tmp = liste
        for i in range (n):
            for j in range (n):
                if(liste[i,j]==1):
                    for k in range(n):
                        if(liste[i,k] == 1):
                            liste[j,k] = 1
                        if(liste[k,j] == 1):
                            liste[k,i] = 1
    i = 1
    while(i<n):
        if(i in tmp2):
            i = i+1
        else :
            for j in range(n):
                if(liste[i,j] == 1):
                    centre2.append(centres[i])
                    centre2.append(centres[j])
                    rayons2.append(rayons[i])
                    rayons2.append(rayons[j])
                    tmp2.append(j)
            i = i+1
            maxre,minre,maxim,minim = rect(centre2,rayons2)
            max_r.append(maxre)
            min_r.append(minre)
            max_i.append(maxim)
            min_i.append(minim)
            centre2 = []
            rayons2 = []
    #Calcule la taille des petits rects
    s = np.size(max_r)
    taille_rect = np.zeros(s)
    for i in range(s):
        taille_rect.itemset(i, (max_r[i] - min_r[i]) * (max_i[i] - min_i[i]))
    #Calcule la taille du grand rect
    grand_rect_max_r, grand_rect_min_r, grand_rect_max_i, grand_rect_min_i = rect(centres,rayons)
    taille_grand_rect = (grand_rect_max_r - grand_rect_min_r) * (grand_rect_max_i - grand_rect_min_i)
    #m_scalar to re-calcule new "m"
    m_scalar = min(taille_rect.item(np.argmax(taille_rect)), taille_grand_rect)/ max( taille_rect.item(np.argmax(taille_rect)), taille_grand_rect)
    return max_r,min_r,max_i,min_i,m_scalar #, max_r_grand_rect,min_r_grand_rect,max_i_grand_rect,min_i_grand_rect
