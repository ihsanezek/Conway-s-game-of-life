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

#Fonction compute_number_neighbors 

def compute_number_neighbors (paded_frame, index_line, index_column) :
    """
    Cette fonction prend en entrée la matrice avec bordure et
    renvoie le nombre de cellules voisines vivantes.
    
    Returns
    -------
    Le nombre de voisin vivant : integer

    """
    
    #On extrait la sous matrice autour de la cellule centrale qui est de dimension 3x3
    neighboors_matrice = paded_frame[index_line - 1 : index_line + 2, index_column - 1 : index_column + 2]
    
    #On compte le nombre de voisins vivant sans oublier de retirer la cellule centrale
    sum_neighboors = numpy.sum(neighboors_matrice) - paded_frame(index_line, index_column)

    return sum_neighboors


#Focntion compute_next_frame

def compute_next_frame (frame): 
    """
    Cette fonction prend en entrée une frame et calcule la frame suivante
    à partir des règles du jeu de la vie
 
    Parameters
    ----------
    frame : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    paded_frame = numpy.pad(frame, 1, mode="constant")
    
    #Etape 1 