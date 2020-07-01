# Elaborar um programa que leia 20 elementos do tipo real em uma matriz A unidimensional e construir uma matriz B de mesma dimensão com os mesmos elementos armazenados na matriz A, porém de forma invertida. Ou seja, o primeiro elemento da matriz A passa a ser o último da matriz B, o segundo elemento da matriz A passa a ser o penúltimo da matriz B e assim por diante. Apresentar os elementos das matrizes A e B.
A = []
B = []
for i in range(0, 5):
  A.append(float(input('Informe o {}° valor real de A: '.format(i + 1))))
B = A
B.sort(reverse=True)
for i in range(0, 5):
  print(B[i])