#  Elaborar um programa que leia 12 elementos numéricos inteiros em uma matriz do tipo vetor. Coloque-os em ordem decrescente e apresente os elementos ordenados. 
A = []
for i in range(0, 12):
    A.append(int(input('informe o {}° valor do vetor A: '.format(i + 1))))
A = sorted(A)
A.sort(reverse = True)
for i in range(0, 12):
    print('A[{}] = {}'.format(i, A[i]))