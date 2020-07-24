# Construir um programa que leia três matrizes A, B e C de uma dimensão do tipo vetor com 15 elementos reais cada. Construir uma matriz D de mesmo tipo e dimensão que seja formada pelo cubo da soma dos elementos correspondentes às matrizes A, B e C. Apresentar a matriz D em ordem crescente.
A = []
B = []
C = []
D = []
for i in range(15):
    A.append(int(input('Informe um valor para a matriz A[{}]: '.format(i))))
for i in range(15):
    B.append(int(input('Informe um valor para a matriz B[{}]: '.format(i))))
for i in range(15):
    C.append(int(input('Informe um valor para a matriz C[{}]: '.format(i))))

for i in range(15):
    D.append((A[i] ** 3) + (B[i] ** 3) + (C[i] ** 3))
C = sorted(C)

for i in range(15):
    print('D[{}] = {}'.format(i, D[i]))
