#  Escrever um programa que leia duas matrizes A e B do tipo vetor com elementos do tipo cadeia, sendo a matriz A com 20 elementos e a matriz B com 30 elementos. Construir uma matriz C, sendo esta a junção das matrizes A e B. Desta forma, a matriz C deve ter a capacidade de armazenar 50 elementos. Apresentar os elementos da matriz C em ordem descendente.
A = []
B = []
C = []
for i in range(20):
    A.append(int(input('Informe um valor para a matriz A[{}]: '.format(i))))
for i in range(30):
    B.append(int(input('Informe um valor para a matriz B[{}]: '.format(i))))
C = A + B
C.sort(reverse = True)
for i in range(50):
    print('C[{}] = {}'.format(i, C[i]))
