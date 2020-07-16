# #  Elaborar um programa que leia 20 elementos para uma matriz qualquer, considerando que essa matriz tenha o tamanho de quatro linhas por cinco colunas, em seguida apresentar a matriz.
A = [[],[], [], []]
for i in range(len(A)):
    for j in range(5):
        A[i].append(input("Informe um valor para o vetor A: "))
for i in range(len(A)):
    for j in range(5):
        print('A[{}][{}] = {}'.format(i, j, A[i][j]))
