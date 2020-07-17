#  Elaborar um programa que leia uma matriz A de duas dimensões com cinco linhas e quatro colunas. Construir uma matriz 8 de mesma dimensão, em que cada elemento seja o fatorial de cada elemento correspondente armazenado na matriz A. Apresentar ao final as matrizes A e B.
A = [[], [], [], [], []]
B = [[], [], [], [], []]
for i in range(len(A)):
    for j in range(4):
        A[i].append(int(input('Informe um valor para matriz A: ')))
for i in range(len(B)):
    for j in range(4):
        n = A[j]
        result = 1
        for x in range(1, n + 1):
            result *= x
        B[i].append(result)
for i in range(len(B)):
    for j in range(4):
        print('B[{}][{}] = {}'.format(i, j, B[i][j]))
