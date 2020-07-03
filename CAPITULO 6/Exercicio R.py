#  Elaborar um programa que leia seis elementos (valores inteiros) para as matrizes A e B de uma dimensão do tipo vetor. Construir as matrizes C e D de mesmo tipo e dimensão. A matriz C deve ser formada pelos elementos de índice ímpar das matrizes A e B e a matriz D deve ser formada pelos elementos de índice par das matrizes A e B. Apresentar os elementos das matrizes C e D. 
A = []
B = []
C = []
D = []
for i in range(0, 6):
    A.append(int(input('Informe o {}° valor de A: '.format(i + 1))))
for i in range(0, 6):
    B.append(int(input('Informe o {}° valor de A: '.format(i + 1))))
for i in range(0, 6):
    if(A[i] % 2 == 1):
        C.append(A[i])
    if(A[i] % 2 == 0):
        D.append(A[i])
    if(B[i] % 2 == 1):
        C.append(B[i])
    if(B[i] % 2 == 0):
        D.append(B[i])
for i in range(0,6):
    print('C[{}] = {} e D[{}] = {}'.format(i + 1, C[i], i + 1, D[i]))