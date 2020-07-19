#  Elaborar um programa que faça a leitura de 20 valores inteiros em uma matriz A de duas dimensões com quatro linhas e cinco colunas. Construir a matriz B de uma dimensão para quatro elementos que seja formada pelo somatório dos elementos correspondentes de cada linha da matriz A. Construir também a matriz C de uma dimensão para cinco elementos que seja formada pelo somatório dos elementos correspondentes de cada coluna da matriz A. Ao final o programa deve apresentar o somatório dos elementos da matriz B com o somatório dos elementos da matriz C.
A = [[], [], [], [], []]
B = []
for i in range(len(A)):
    for j in range(4):
        A[i].append(int(input('Informe um valor para A[{}][{}]: '.format(i, j))))
for i in range(5):
    soma = 0
    for j in range(4):
        soma += A[i][j]
    B.append(soma)
for i in range(5):
    soma = 0
    for j in range(4):
        soma += A[i][j]
    C.append(soma)
print('='*70)
for i in range(4):
    print('B[{} = {}'.format(i, B[i]))
print('='*70)
for i in range(4):
    print('C[{} = {}'.format(i, C[i]))
