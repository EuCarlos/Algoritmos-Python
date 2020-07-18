#  Elaborar um programa que leia uma matriz A do tipo real de duas dimensões com oito linhas e seis colunas. Construir a matriz 8 de uma dimensão que seja formada pela soma de cada linha da matriz A. Ao final apresentar o somatório dos elementos da matriz B.
A = [[], [], [], [], [], [] , [], []]
B = []
for i in range(len(A)):
    for j in range(6):
        A[i].append(int(input('Informe um valor para A[{}][{}]: '.format(i, j))))
for i in range(8):
    soma = 0
    for j in range(6):
        soma += A[i][j]
    B.append(soma)
for i in range(8):
    print('B[{}] = {}'.format(i, B[i]))
