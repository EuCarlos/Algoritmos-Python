# Ler dois valores numéricos inteiros (representados pelas variáveis A e B) e apresentar o resultado do quadrado da diferença do primeiro valor (variável A) em relação ao segundo valor (variável B) 
A = int(input('Informe valor de A: '))
B = int(input('Informe valor de B: '))
X = (A - B)**2
print('O Quadrado da diferença é {}'.format(X))