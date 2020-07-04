#  Elaborar um programa que leia uma matriz A de uma dimensão com seis elementos do tipo real. Construir uma matriz B, em que cada posição de índice ímpar da matriz B deve ser atribuída com um elemento de índice par existente na matriz A e cada posição de índice par da matriz B deve ser atribuída com um elemento de índice ímpar existente na matriz A. Apresentar os elementos das duas matrizes
A = []
for i in range(0, 6):
    A.append(float(input('informe o {}° numero real do vetor A: '.format(i + 1))))
for i in range(0, 6):
    if(i % 2 == 1):
        B.append(A[i + 1]) 
    else:
        B.append(A[i - 1])
for i in range(0, 6):
    print('A[{}] = {} e B[{}] = {}'.format(i + 1, A[i], i + 1, B[i]))