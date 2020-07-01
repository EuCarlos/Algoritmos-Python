#  Elaborar um programa que leia uma matriz A do tipo vetor com 20 elementos inteiros. Construir uma matriz B do mesmo tipo e dimensão da matriz A, sendo cada elemento da matriz B o somatório de 1 até o valor do elemento correspondente armazenado na matriz A. Se o valor do elemento da matriz A[1] for 5, o elemento correspondente da matriz B[1] deve ser 15, pois o somatório do elemento da matriz A é 1 +2+3+4+5. Apresentar os elementos da matriz B.
A = []
B = []
for i in range(0, 20):
    A.append(int(input('Informe {}° valor de A: '.format(i + 1))))
for i in range(0, 20):
    soma = 0
    cont = 1
    for x in range(0, A[i]):
        soma = soma + cont
        cont = cont + 1
    B.append(soma)
for i in range(0, 20):
    print(B[i])