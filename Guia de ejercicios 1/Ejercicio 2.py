#Referencia
#Se tiene una matriz A, donde la matriz inversa de A se representa como A−1
#la cual es una matriz cuadrada que hace que la multiplicacion´ A × A−1
#sea igual a la matriz. identidad I. Realizar un algoritmo que compruebe la siguiente propiedad:
#A × A −1 = I, donde I es la Matriz Identidad


import numpy as np

# Definir la matriz A
A = np.array([[2, 1], [4, 3]])

# Calcular la matriz inversa de A
A_inversa_matriz = np.linalg.inv(A)   #el np.linalg.inv es el valor devuelto, tambien es una matriz

# Calcular el producto de A por A inversa
resultado = np.dot(A, A_inversa_matriz)

# Obtener la matriz identidad
I = np.eye(len(A))

# Comprobar si el resultado es igual a la matriz identidad
if np.array_equal(resultado, I):
    
    print ("La propiedad se respeta: A * A⁻¹ = I")     #La propiedad es A * A-1 = I
else:
    print ("La propiedad no se respeta, incorrecto: A * A⁻¹ ≠ I")  ##La propiedad no es A * A-1 = I