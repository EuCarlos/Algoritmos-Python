#   Elaborar um programa que leia uma matriz A do tipo inteira de duas dimensões com sete linhas e sete colunas. Construir a matriz B de mesma dimensão, em que cada elemento seja o somatório de 1 até o valor armazenado na posição da matriz A, com exceção dos valores situados nos índices ímpares da diagonal principal (B[1,1), B[3,3), B[5,5) e B[7,7)), os quais devem ser o fatorial de cada elemento correspondente da matriz A. Apresentar ao final a matriz B.

A = [[], [], [], [], [], [], []]
B = [[], [], [], [], [], [], []]
for i in range(len(A)):
    for j in range(7):
        A[i].append(int(input('Informe um valor para a matriz A: ')))
for i in range(len(B)):
    for j in range(7):
        if((i % 2 == 1) and (i == j)):
            n = A[i][j]
            result = 1
            for x in range(1, n + 1):
                result *= x
            B[i].append(result)
        else:
            somat = 0
            cont = 1
            for x in range(0, A[j][i]):
                somat = somat + cont
                cont = cont + 1
            B[i].append(somat)
for i in range(len(B)):
    for j in range(7):
        print('B[{}][{}] = {}'.format(i, j, B[i][j]))
