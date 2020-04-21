# Elaborar um programa que calcule e apresente o valor do volume de uma caixa retangular, utilizando a fórmula VOLUME <- COMPRIMENTO* LARGURA* ALTURA. 
comp = int(input('Informe o comprimento: '))
larg = int(input('Informe a largura: '))
alt = int(input('Informe a altura: '))
vol = comp * larg * alt
print('O volume da caixa é de {}'.format(vol))