#  Elaborar um programa que leia duas matrizes A e B do tipo vetor com 15 elementos inteiros cada. Construir duas outras matrizes C e D de mesmo tipo. Cada elemento da matriz C deve ser o somatório do elemento correspondente da matriz A, e cada elemento da matriz D deve ser o fatorial do elemento correspondente da matriz B. Em seguida construir uma matriz E, que deve conter a diferença dos elementos das matrizes C e D com a soma dos elementos das matrizes A e B. Apresentar os elementos da matriz E em ordem crescente.
A = []
B = []
C = []
D = []
E = []
for i in range(15):
    A.append(int(input('Informe um valor para a matriz A[{}]: '.format(i))))
for i in range(15):
    B.append(int(input('Informe um valor para a matriz B[{}]: '.format(i))))

for i in range(15):
    somat = 0
    cont = 1
    for x in range(0, A[i]):
        somat = somat + cont
        cont = cont + 1
    C.append(somat)

for i in range(15):
    n = A[i]
    result = 1
    for x in range(1, n + 1):
        result *= x
    D.append(result)

for i in range(15):
    E.append((C[i] - D[i]) + (A[i] + B[i]))

E = sorted(E)
print('='*70)
for i in range(15):
    print('E[{}] = {}'.format(i, E[i]))
