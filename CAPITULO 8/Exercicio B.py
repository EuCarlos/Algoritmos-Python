#  Elaborar um programa que leia duas matrizes A e B, cada uma com uma dimensão para sete elementos inteiros. Construir uma matriz C de duas dimensões, cuja primeira coluna deve ser formada pelos elementos da matriz A e a segunda coluna pelos elementos da matriz B. Apresentar a matriz C.
A = []
B = []
C = [[], []]
for i in range(7):
    A.append(int(input('Informe um valor para a matriz A: ')))
for i in range(7):
    B.append(int(input('Informe um valor para a matriz B: ')))
for i in range(1):
    for j in range(7):
        C[i].append(A[j])
for i in range(1, 2):
    for j in range(7):
        C[i].append(B[j])
for i in range(len(C)):
    for j in range(7):
        print('C[{}][{}] = {}'.format(i, j, C[i][j]))
