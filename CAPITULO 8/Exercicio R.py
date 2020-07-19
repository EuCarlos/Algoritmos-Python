# Elaborar um programa que leia quatro matrizes A, B, C e D de uma dimensão com quatro elementos. Construir uma matriz E de duas dimensões do tipo 4 x 4, sendo a primeira linha formada pelo dobro dos valores dos elementos da matriz A, a segunda linha formada pelo triplo dos valores dos elementos da matriz B, a terceira linha formada pelo quádruplo dos valores dos elementos da matriz C e a quarta linha formada pelo fatorial dos valores dos elementos da matriz D. Apresentar a matriz E.
A = []
B = []
C = []
D = []
E = [[], [], [], []]
for i in range(4):
    A.append(int(input('Informe um valor para a matriz A: ')))
for i in range(4):
    B.append(int(input('Informe um valor para a matriz B: ')))
for i in range(4):
    C.append(int(input('Informe um valor para a matriz C: ')))
for i in range(4):
    D.append(int(input('Informe um valor para a matriz D: ')))

for i in range(1):
    for j in range(4):
        E[i].append(A[j] * 2)
for i in range(1, 2):
    for j in range(4):
        E[i].append(B[j] * 3)
for i in range(2, 3):
    for j in range(4):
        E[i].append(B[j] * 4)
for i in range(3, 4):
    for j in range(4):
        n = D[j]
        result = 1
        for x in range(1, n + 1):
            result *= x
        E[i].append(result)

print('='*70)
for i in range(len(E)):
    for j in range(4):
        print('D[{}][{}] = {}'.format(i, j, E[i][j]))
