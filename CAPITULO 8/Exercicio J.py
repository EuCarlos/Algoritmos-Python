#  Elaborar um programa que leia uma matriz A de duas dimensões com seis linhas e cinco colunas. Construir a matriz B de mesma dimensão, que deve ser formada do seguinte modo: para cada elemento par da matriz A deve ser somado 5 e de cada elemento ímpar da matriz A deve ser subtraído 4. Apresentar ao final as matrizes A e B
A = [[], [], [], [], [], []]
B = [[], [], [], [], [], []]
for i in range(len(A)):
    for j in range(5):
        A[i].append(int(input('Informe um valor para a Matriz A: ')))
for i in range(len(B)):
    for j in range(5):
        if(A[i][j] % 2 == 0):
            B[i].append(A[i][j] + 5)
        else:
            B[i].append(A[i][j] - 4)
for i in range(len(B)):
    for j in range(5):
        print('A[{}][{}] = {} e B[{}][{}] = {}'.format(i, j, A[i][j], i, j, B[i][j]))
