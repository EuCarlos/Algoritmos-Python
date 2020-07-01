#  Elaborar um programa que leia duas matrizes do tipo vetor para o armazenamento de nomes de pessoas, sendo a matriz A com 20 elementos e a matriz B com 30 elementos. Construir uma matriz C, sendo esta a junção das matrizes A e B. Desta forma, a matriz C deve ter a capacidade de armazenar 50 elementos. Apresentar os elementos da matriz C.
A = []
B = []
C = []
for i in range(0, 20):
  A.append(int(input('Informe o {}° Valor do vetor A: '.format(i + 1))))
for i in range(0, 30):
  B.append(int(input('Informe o {}° Valor do vetor B: '.format(i + 1))))
C = A + B
for x in range(0, 50):
  print('C[{}] = {}'.format(x + 1, C[x]))