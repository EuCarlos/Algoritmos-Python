#  Elaborar um programa que leia 15 elementos inteiros em uma matriz A. Construir uma matriz B de mesmo tipo e tamanho, em que cada elemento da matriz B seja a metade absoluta de cada elemento da matriz A. Apresentar os elementos da matriz A em ordem decrescente e os de B em ordem crescente.
A = []
B = []
for i in range(15):
    A.append(int(input('Informe um valor para a matriz A[{}]: '.format(i))))
for i in range(15):
    B.append(A[i] / 2)

print('='*70)
A = sorted(A)
A.sort(reverse = True)
for i in range(15):
    print('A[{}] = {}'.format(i, A[i]))

print('='*70)
B = sorted(B)
for i in range(15):
    print('B[{}] = {}'.format(i, B[i]))
