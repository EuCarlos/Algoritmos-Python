# Elaborar um programa que leia duas matrizes A e B de uma dimensão com seis elementos. A matriz A deve aceitar apenas a entrada de valores pares, enquanto a matriz B deve aceitar apenas a entrada de valores ímpares. A entrada das matrizes deve ser validada pelo programa e não pelo usuário. Construir uma matriz C que seja o resultado da junção das matrizes A e B, de modo que a matriz C contenha 12 elementos. Apresentar os elementos da matriz C.
A = []
B = []
C = []
for i in range(0, 6):
    A[i] = 1
    while(A[i] % 2 == 0):
        A.append(int(input('Informe o {}° valor do vetor A'.format(i + 1))))
for i in range(0, 6):
    B[i] = 0
    while(A[i] % 2 == 1):
        B.append(int(input('Informe o {}° valor do vetor B'.format(i + 1))))
C = A + B
for i in range(0, 12):
    print('C[{}] = {}'.format(i + 1, C[i]))