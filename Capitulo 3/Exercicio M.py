# Construir um programa que leia três valores numéricos inteiros (representados pelas variáveis A, B e C) e apresente como resultado final o valor da soma dos quadrados dos três valores lidos. 
A = int(input('Informe valor de A: '))
B = int(input('Informe valor de B: '))
C = int(input('Informe valor de C: '))
SomaQ = (A**2)+(B**2)+(C**2)
print('O resultado das soma dos quadrados é igual a {}'.format(SomaQ))