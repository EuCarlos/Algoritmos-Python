#  Elaborar um programa que leia uma matriz A com 12 elementos do tipo real. Após a leitura da matriz A, colocar os seus elementos em ordem crescente. Depois, fazer a leitura de uma matriz B também com 12 elementos do tipo real e colocar os elementos em ordem crescente. Construir uma matriz C, em que cada elemento seja a soma do elemento correspondente das matrizes A e B. Colocar em ordem decrescente os elementos da matriz C e apresentar os seus valores.
A = []
B = []
C = []
for i in range(12):
    A.append(float(input('Informe um valor para a matriz A[{}]: '.format(i))))
A = sorted(A)
for i in range(12):
    B.append(float(input('Informe um valor para a matriz B[{}]: '.format(i))))
B = sorted(B)

for i in range(12):
    C.append(A[i] + B[i])
C.sort(reverse = True)

for i in range(12):
    print('C[{}] = {}'.format(i, C[i]))
