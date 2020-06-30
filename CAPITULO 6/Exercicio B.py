# Elaborar um programa que leia oito elementos inteiros em uma matriz A do tipo vetor. Construir uma matriz B de mesma dimensão com os elementos da matriz A multiplicados por 3. O elemento 8[1] deve ser implicado pelo elemento A[1] * 3, o elemento 8[2] implicado pelo elemento A[2] * 3 e assim por diante, até 8. Apresentar a matriz 8. 
A = []
B = []
for i in range(1, 9):
  A.append(int(input('informe o {}° valor de A: '.format(i))))
for x in range(len(A)):
  B.append(A.index(x + 1) * 3)
for y in range(len(B)):
  print(B[y + 1])