#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 03:58:24 2018

@author: ta
"""

import matplotlib.pyplot as plt
"""
plt.ylabel('temps')
plt.xlabel('taille de la matrice')
plt.plot([8,7,6,5,4,3,2], [43,37,32,27,23,20,18], 'ob-', label='Parallel')
plt.plot([8,7,6,5,4,3,2], [98,87,73,64,57,49,43], 'or-', label='Sequentiel')
plt.legend()
plt.savefig('grand_rect.png', transparent=False, bbox_inches='tight')
plt.show()
"""

plt.ylabel('temps')
plt.xlabel('taille de la matrice')
plt.plot([8,7,6,5,4,3,2], [65,77,25,19,51,51,25], 'ob-', label='Petits rects sequentiel')
plt.plot([8,7,6,5,4,3,2], [36,42,14,10,28,50,25], 'ob--', label='Petits rects parallel')
plt.plot([8,7,6,5,4,3,2], [96,83,72,62,55,50,43], 'or-', label='Grand rect sequentiel')
plt.plot([8,7,6,5,4,3,2], [42,35,31,27,23,20,18], 'or--', label='Grand Rect parallel')


plt.legend()
plt.savefig('petits_grand.png', transparent=False, bbox_inches='tight')
plt.show()
