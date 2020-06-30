#  Escrever um programa que leia duas matrizes (denominadas A e B) do tipo vetor com 20 elementos reais. Construir uma matriz C, sendo cada elemento da matriz C a subtração de um elemento correspondente da matriz A com um elemento correspondente da matriz B, ou seja, a operação de processamento deve estar baseada na operação C[I] +- A[I] – B[1]. Ao final, apresentar os elementos da matriz C. 
A = []
B = []
C = []
for i in range(0, 20):
  A.append(int(input('Digite {}° valor do vetor A: '.format(i + 1))))
for y  in range(0, 20):
  B.append(int(input('Digite {}° valor do vetor B: '.format(y + 1))))
for x in range(len(B)):
  C.append(A[x] - B[x])
for z in range(len(B)):
  print(C[z])