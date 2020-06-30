#  Elaborar um programa que leia 15 elementos inteiros de uma matriz A do tipo vetor. Construir uma matriz B demesmo tipo, observando a seguinte lei de formação: "todo elemento da matriz B deve ser o quadrado do elemento da matriz A correspondente". Apresentar os elementos das matrizes A e B. 
A = []
B = []
for i in range(0, 15):
  A.append(int(input('Informe {}° do vetor A: '.format(i + 1))))
for x in range(len(A)):
  B.append(A[x] ** 2)
for y in range(0, 15):
  print('A[{}] e B[{}]'.format(A[y], B[y]))