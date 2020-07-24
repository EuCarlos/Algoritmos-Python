#  Elaborar um programa que leia duas matrizes A e B de uma dimensão do tipo vetor com dez elementos inteiros cada. Construir uma matriz C de mesmo tipo e dimensão, que seja formada pela soma dos quadrados de cada elemento correspondente das matrizes A e B. Apresentar a matriz C em ordem decrescente.
A = []
B = []
C = []
for i in range(10):
    A.append(int(input('Informe um valor para a matriz A[{}]: '.format(i))))
for i in range(10):
    B.append(int(input('Informe um valor para a matriz B[{}]: '.format(i))))

for i in range(10):
    C.append((A[i] ** 2) + (B[i] ** 2))

C = sorted(C)
C.sort(reverse = True)
print('='*70)
for i in range(10):
    print('C[{}] = {}'.format(i, C[i]))
