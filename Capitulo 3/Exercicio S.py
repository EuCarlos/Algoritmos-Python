# Elaborar um programa que leia dois valores numéricos reais desconhecidos representados pelas variáveis A e B. Calcular e apresentar os resultados das quatro operações aritméticas básicas. 
A = float(input('informe valor de A: '))
B = float(input('informe valor de B: '))
Soma = A + B
Subt = A - B
Mult = A * B
Divi = A / B
print(' Soma: {} \n Subtração: {} \n Multiplicação: {} \n Divisão: {}'.format(Soma, Subt, Mult, Divi))