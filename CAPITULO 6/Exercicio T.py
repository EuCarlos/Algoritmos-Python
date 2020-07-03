# Escrever um programa que leia duas matrizes A e B de uma dimensão com dez elementos. A matriz A deve aceitar apenas a entrada de valores divisíveis por 2 e 3, enquanto a matriz B deve aceitar apenas a entrada de valores múltiplos de 5. A entrada das matrizes deve ser validada pelo programa e não pelo usuário. Construir uma matriz C que seja o resultado da junção das matrizes A e B, de modo que contenha 20 elementos. Apresentar os elementos da matriz C. 
def zeraIndice():
    i = 0
A = []
B = []
C = []
for i in range(0, 10):
    while(not(A[i] % 2 == 0) and not(A[i] % 3 ==0)):
        A.append(int(input('Informe o {} valor do vetor A: '.format(i + 1))))
for i in range(0, 10):
    while not(B[i] % 5 == 0):
        B.append(int(input('Informe o {} valor do vetor B: '.format(i + 1))))
C = A + B
for i in range(0, 20):
    print('C[{}] = {}'.format(C[i]))
