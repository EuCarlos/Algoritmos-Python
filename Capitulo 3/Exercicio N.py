# Construir um programa que leia três valores numéricos inteiros (representados pelas variáveis A, B e C) e apresente como resultado final o valor do quadrado da soma dos três valores lidos. 
A = int(input('Informe valor de A: '))
B = int(input('Informe valor de B: '))
C = int(input('Informe valor de C: '))
QSoma = (A + B + C)**2
print('O resultado do quadrado da soma é igual a {}'.format(QSoma))