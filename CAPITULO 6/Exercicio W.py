#  Elaborar um programa que leia duas matrizes A e B de uma dimensão do tipo vetor com dez elementos inteiros cada. Construir uma matriz C de mesmo tipo e dimensão que seja formada pelo quadrado da soma dos elementos correspondentes nas matrizes A e B. Apresentar os elementos da matriz C. 
A = []
B = []
C = []
for i in range(0, 10):
    A.append(int(input('Informe o {}° valor de A: '.format(i + 1))))
for i in range(0, 10):
    B.append(int(input('Informe o {}° valor de B: '.format(i + 1))))
for i in range(0, 10):
    C.append((A[i] + B[i])**2)
for i in range(0, 10):
    print('C[{}] = {}'.format(i + 1, C[i]))
