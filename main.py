# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 14:45:06 2024

@author: 33785
"""
#importation de la bibliothèque numpy
import numpy 

#création de la  matrice de dimension (7, 7) avec des valeurs égales à 0 si la cellule est morte et à 1 si elle est vivante 
frame = numpy.array([[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]])

print (frame)