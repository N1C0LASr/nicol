import random

def print_matrix(mat):
    for row in mat:
        print(' '.join(format(item, "10.4f") for item in row))

#funcion para generar una matriz cuadrada

def random_matrix(n):
    return [[random.random() for j in range(n)] for i in range(n)]

# Función para invertir una matriz usando Eliminación de Gauss

def gauss_invert(mat):
    n = len(mat)

#crear la matriz aumentada

    aug_mat = [row + [float(i == j) for j in range(n)] for i, row in enumerate(mat)]

#realizar la Eliminación de Gauss

    for i in range(n):
        max_row = max(range(i, n), key=lambda j: abs(aug_mat[j][i]))
        aug_mat[i], aug_mat[max_row] = aug_mat[max_row], aug_mat[i]

#normalizando

        div = aug_mat[i][i]
        for j in range(i, 2 * n):
            aug_mat[i][j] /= div

#reduciendo

        for j in range(n):

            if j != i:
                mult = aug_mat[j][i]
                for k in range(i, 2 * n):
                    aug_mat[j][k] -= mult * aug_mat[i][k]

#extraer la matriz inversa

    return [row[n:] for row in aug_mat]

#Generar una matriz cuadrada aleatoria de dimensión n

n = random.randint(3, 5)
A = random_matrix(n)

print("Original matrix A:")
print_matrix(A)
print("Inverse of A:")
print_matrix(gauss_invert(A))

#fin