#  Elaborar um programa que leia uma matriz A do tipo inteira de duas dimensões com cinco linhas e cinco colunas. Construir uma matriz 8 de mesma dimensão, em que cada elemento seja o dobro de cada elemento correspondente da matriz A, com exceção dos valores situados na diagonal principal (posições B[1, 1 ], B[2,2), B[3,3), B[4,4) e B[5,5)), os quais devem ser o triplo de cada elemento correspondente da matriz A. Apresentar ao final a matriz B.
A = [[], [], [], [], []]
B = [[], [], [], [], []]
for i in range(len(A)):
    for j in range(5):
        A[i].append(int(input('Informe um valor para a matriz A: ')))
for i in range(len(B)):
    for j in range(5):
        if(i == j):
            B[i].append(A[i][j] * 3)
        else:
            B[i].append(A[i][j] * 2)
for i in range(len(B)):
    for j in range(5):
        print('B[{}][{}] = {}'.format(i, j, B[i][j]))
