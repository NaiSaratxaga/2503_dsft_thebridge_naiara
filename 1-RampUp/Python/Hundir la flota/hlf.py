import os
import time
# Crear un tablero como una lista de listas de 10x10 que contenga caracteres espacios:""
# Aquí estamos creando una lista vacía llamada tablero, que será la que contenga todas las filas del tablero.
tablero = []
num_columnas = 10
num_filas = 10
#Este bucle for se ejecuta 10 veces, es decir, crea 10 filas para el tablero. Cada fila será una lista que tiene 10 espacios vacíos.
for indice_fila in range(num_filas):
#Dentro de cada iteración del bucle, creamos una nueva lista llamada linea. Luego, dentro de otro bucle for (también de 10 repeticiones),
# agregamos 10 espacios vacíos (" ") a esta lista. Cada espacio representa una celda en esa fila del tablero.
    linea = []
    for indice_columna in range(num_columnas):
        if (indice_fila == 1 and indice_columna < 4) or (indice_columna == 3 and (indice_fila >= 3 and indice_fila <= 5)):
            linea.append("B")
        else:
            linea.append(" ")
#Después de crear la fila (es decir, después de añadir 10 espacios vacíos), esta fila se añade a la lista principal tablero.
    tablero.append(linea)
#Al final del proceso, tablero tendrá 10 listas, cada una de ellas con 10 espacios vacíos, lo que crea un tablero de 10x10 de celdas vacías.
tablero

# Escribir una celda de código separada de las anteriores para simular que el usuario está efectuando un disparo: 
# - Solicite al usuario dos coordenadas `i,j` mediante dos inputs

