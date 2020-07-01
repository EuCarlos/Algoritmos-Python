# Construir um programa que leia duas matrizes A e B do tipo vetor com 15 elementos quaisquer inteiros. Construir uma matriz C, sendo esta o resultado da junção das matrizes A e B. Desta forma, a matriz C deve ter o dobro de elementos em relação às matrizes A e B, ou seja, a matriz C deve possuir 30 elementos. Apresentar a matriz C.
A = []
B = []
C = []
for i in range(1, 16):
  A.append(int(input('Informe o {}° valor do vetor A: '.format(i))))
for i in range(1, 16):
  B.append(int(input('Informe o {}° valor do vetor B: '.format(i))))
C = A + B
for x in range(0, 30):
  print('C[{}] = {}'.format(x + 1, C[x]))