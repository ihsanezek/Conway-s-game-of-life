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
    
    """
    # Étape 1 : 2 boucles for imbriquées pour parcourir la matrice avec bordure (zero padding) element par element.
       Faites attention à l'index de début et d'arrêt ! (il s'agit de la matrice avec bordure)
    """   
   
    #ici je définis ma matrice avec les bordures
    index_line, index_column = paded_frame.shape

    # Parcourir la matrice en ligne et en colonne en prenant en compte le fait qu'il y ait des bordures de 0  
    for line in range (2, index_line - 2) : 
        for column in range (2, index_column - 2) :                                                  
            """
            # Étape 2 : Pour chacun des éléments, calculez le nombre de voisins.
            On fait appelle à la fonction (compute_number_neighbors)
            """
            total_living_neighboors = compute_number_neighbors(paded_frame, index_line, index_column)
            new_frame = numpy.zeros_like(frame)
            
            """
             # Étape 3 : Pour chacun des éléments faire les tests (état de l'élément et son nombre de voisin) afin de voir
             si il y a des modifications à faire.
             Si c'est le cas effectuez les modifications directement dans la matrices frame (Attention à l'indice
             utilisé ! )
            """
            if paded_frame [line, column] == 1 :
                if total_living_neighboors in [2, 3] : 
                    new_frame [line - 1, column - 1] = 1 #la cellule reste vivante
                else :
                    new_frame [line - 1, column - 1] = 0 #La cellule meurt
            else : 
                if total_living_neighboors == 3 : 
                    new_frame = [line - 1, column - 1] = 1 #La cellule qui était initiallement morte devient vivante car elle a exactement 3 voisins vivants 
                
                    
                    
                    
                
            
    return frame


while True:
# boucle infini qui affiche toutes les frames successives (ctrl + c pour arrêter le script)
    print(frame)
    frame = compute_next_frame(frame)