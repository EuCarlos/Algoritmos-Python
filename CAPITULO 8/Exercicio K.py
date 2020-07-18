# Elaborar um programa que leia uma matriz A do tipo real de duas dimensões com cinco linhas e cinco colunas. Apresentar o somatório dos elementos situados na diagonal principal (posições A[1, 1 ], A[2,2], A[3,3], A[4,4] e A[5,5]) da referida matriz.
A = [[], [], [], [], []]
for i in range(len(A)):
    for j in range(5):
        A[i].append(int(input('Informe um valor para a matriz A[{}][{}]: '.format(i, j))))
for i in range(len(A)):
    for j in range(5):
        if (i == j):
            somat = 0
            cont = 1
            for x in range(0, A[i][j]):
                somat = somat + cont
                cont = cont + 1
            A[i][j] = somat
for i in range(len(A)):
    for j in range(5):
        if (i == j):
            print('A[{}][{}] = {}'.format(i, j, A[i][j]))
