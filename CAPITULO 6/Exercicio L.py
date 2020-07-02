# Elaborar um programa que leia uma matriz A do tipo vetor com dez elementos inteiros. Construir uma matriz B de mesmo tipo, em que cada elemento deve ser a metade exata de cada um dos elementos existentes da matriz A. Apresentar os elementos das matrizes A e B.
A = []
B = []
for i in range(0, 10):
    A.append(float(input('Digite o {}° do vetor A: '.format(i + 1))))
for i in range(0, 10):
    B.append(A[i] / 2)
for i in range(0, 10):
    print('A[{}] = {} e sua metade é B[{}] = {}'.format(i + 1, i + 1, A[i], B[i]))