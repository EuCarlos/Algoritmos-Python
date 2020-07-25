# Elaborar um programa que leia uma matriz A com dez elementos do tipo cadeia. Construir uma matriz B de mesma dimensão e tipo que a matriz A. O último elemento da matriz A deve ser o primeiro da matriz B, o penúltimo elemento da matriz A deve ser o segundo da matriz B até que o primeiro elemento da matriz A seja o último da matriz B. Apresentar os elementos da matriz B de forma ordenada ascendente.
A = []
B = []
for i in range(10):
    A.append(str(input('Informe elementos para a matriz A[{}]: '.format(i))))
B = A
B.reverse()
print(B)
