#  Elaborar um programa que leia três matrizes A, B e C de uma dimensão do tipo vetor com 15 elementos inteiros cada. Construir uma matriz D de mesmo tipo e dimensão que seja formada pela soma dos elementos correspondentes às matrizes A, B e C. Montar o trecho de pesquisa binária para pesquisar os elementos existentes na matriz D.
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
    D.append(A[i] + B[i] + C[i])
C = sorted(C)

for i in range(15):
    print('D[{}] = {}'.format(i, D[i]))
