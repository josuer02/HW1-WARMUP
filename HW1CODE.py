# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 11:36:21 2022

@author: josue
"""

Lista = []

NumLista = int(input("Ingrese el numero de elementos que desea en la lista: "))

for i in range(1, NumLista+1):
    DatosLista = int(input("Ingrese los datos: "))
    Lista.append(DatosLista)
    
    
print("El segundo elemento mas grande en la lista es: ", sorted(Lista)[-2])

    
    
    
