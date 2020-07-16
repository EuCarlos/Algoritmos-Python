#  Elaborar um programa que leia uma matriz A de uma dimensão com dez elementos inteiros. Construir uma matriz C de duas dimensões com três colunas, sendo a primeira coluna da matriz C formada pelos elementos da matriz A somados com 5, a segunda coluna seja formada pelo valor do cálculo da fatorial de cada elemento correspondente da matriz A, e a terceira e última coluna pelos quadrados dos elementos correspondentes da matriz A. Apresentar a matriz C
A = []
C= [[], [], []]
for i in range(10):
    A.append(int(input('Informe um valor para matriz A: ')))
for i in range(1):
    for j in range(10):
        C[i].append(int(A[j] + 5))
for i in range(1, 2):
    for j in range(10):
        n = A[j]
        result = 1
        for x in range(1, n + 1):
            result *= x
        C[i].append(result)
for i in range(2, 3):
    for j in range(10):
        C[i].append(int(A[j] ** 2))
print('='*40)
for i in range(len(C)):
    for j in range(7):
        print('C[{}][{}] = {}'.format(i, j, C[i][j]))
