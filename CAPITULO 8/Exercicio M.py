#  Elaborar um programa que leia uma matriz A do tipo real de duas dimensões com cinco linhas e cinco colunas. Apresentar o somatório dos elementos situados nas posições de linha e coluna ímpares da diagonal principal (A[1, 1 ], A[3,3], A[5,5]) da referida matriz.
A = [[], [], [], [] ,[]]
for i in range(len(A)):
    for j in range(5):
        A[i].append(int(input('Informe um valor para A[{}][{}]: '.format(i, j))))
for i in range(len(A)):
    for j in range(5):
        if ((i == j) and (A[i][j] % 2 == 1)):
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
