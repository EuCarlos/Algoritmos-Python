# Elaborar um programa que leia quatro valores numéricos inteiros (variáveis A, B, C e D). Ao final o programa deve apresentar o resultado do produto (variável P) do primeiro com o terceiro valor, e o resultado da soma (variável S) do segundo com o quarto valor. 
A = int(input('Informe o valor de A:'))
B = int(input('Informe o valor de B:'))
C = int(input('Informe o valor de C:'))
D = int(input('Informe o valor de D:'))
P = A + C
S=  B + D
print('Valor de P é {} e o Valor de S é {}'.format(P, S))