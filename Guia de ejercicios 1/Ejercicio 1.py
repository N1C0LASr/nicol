#referencia

#Crear una matriz cuadrada de 5 × 5, y 
#obtener la suma de todos los elementos de cada columna, 
#e imprimir la suma mas alta entre las columnas. 
#Ademas obtener la suma de todos los elementos de las filas 
#y la suma mas baja entre todas las filas. 
#Sin utilizar la biblioteca numpy.

from random import randint

columnas = 5
filas = 5

matrices= [[randint(0,5) * int(all(
    [i, i < columnas - 1, j, j < filas - 1])) 
      for i in range(columnas)] 
      for j in range(filas)]

for m in matrices:
    print(m)

resultado = matrices[0][:]

for matriz in matrices[1:]:
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            resultado[i][j] += matriz[i][j]

#la fila se imprime

for fila in resultado:
    print(fila)