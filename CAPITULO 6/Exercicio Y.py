# Escrever um programa que leia uma matriz A de uma dimensão com 15 elementos numéricos inteiros. Apresentar o total de elementos pares existentes na matriz.
A = []
Par = 0
for i in range(0, 15):
    A.append(int(input('Informe o {}° valor de A: '.format(i +1))))
    if(A[i] % 2 == 0):
        Par = Par + 1
print('O total de numeros PARES informados é igual a ',Par)