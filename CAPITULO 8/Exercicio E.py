# Elaborar um programa que leia duas matrizes A e B, cada uma com uma dimensão para 12 elementos reais. Construir uma matriz C de duas dimensões, sendo a primeira coluna da matriz C formada pelos elementos da matriz A multiplicados por 2 e a segunda coluna formada pelos elementos da matriz B subtraídos de 5. Apresentar separadamente as matrizes.
A = []
B = []
C = [[], []]
for i in range(7):
    A.append(float(input('Informe um valor para a matriz A: ')))
for i in range(7):
    B.append(float(input('Informe um valor para a matriz B: ')))

for i in range(1):
    for j in range(7):
        C[i].append(A[j] * 2)
for i in range(1, 2):
    for j in range(7):
        C[i].append(B[j] - 5)
for i in range(len(C)):
    for j in range(7):
        print('C[{}][{}] = {}'.format(i, j, C[i][j]))
