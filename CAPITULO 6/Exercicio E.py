#  Elaborar um programa que leia uma matriz A do tipo vetor com 15 elementos inteiros. Construir uma matriz B de mesmo tipo, e cada elemento da matriz B deve ser o resultado da fatorial correspondente de cada elemento da matriz A. Apresentar as matrizes A e B. 
A = []
B = []
for i in range(0, 15):
  A.append(int(input('informe o {}° valor de A: '.format(i + 1))))
for i in range(0,15):
  B.append(1)
  for y in range(1, A[i]):
    B[i] = B[i] * y
  B.append(B[i])
print('_________________________________________')
for z in range(0, 15):
  print('{}! é igual a {}'.format(A[z], B[z + 1]))
print('_________________________________________')