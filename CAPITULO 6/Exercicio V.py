# Construir um programa que leia uma matriz A de uma dimensão do tipo vetor com 30 elementos do tipo inteiro.Ao final do programa, apresentar a quantidade de valores pares e ímpares existentes na referida matriz. 
A = []
Par = 0
Impar = 0
for i in range(0, 30):
    A.append(int(input('Informe o {}° valor do vetor A: '.format(i + 1))))
    if(A[i] % 2 == 0):
        Par = Par + 1
    else:
        Impar = Impar + 1
print('Há {} valores PARES e {} valores IMPARES'.format(Par, Impar))