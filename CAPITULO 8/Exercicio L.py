#  Elaborar um programa que leia uma matriz A de duas dimensões com 15 linhas e 15 colunas. Apresentar o somatório dos elementos pares situados na diagonal principal da referida matriz.
A = [[], [], [], [] ,[], [], [], [], [] ,[], [], [], [], [] ,[]]
for i in range(len(A)):
    for j in range(15):
        A[i].append(int(input('Informe um valor para A[{}][{}]: '.format(i, j))))
for i in range(len(A)):
    for j in range(15):
        if ((i == j) and (A[i][j] % 2 == 0)):
            somat = 0
            cont = 1
            for x in range(0, A[i][j]):
                somat = somat + cont
                cont = cont + 1
            A[i][j] = somat
for i in range(len(A)):
    for j in range(15):
        if (i == j):
            print('A[{}][{}] = {}'.format(i, j, A[i][j]))
