# Elaborar um programa que leia dez valores numéricos reais e apresente no final o somatório e a média dos valores lidos. 
soma = 0
cont = 1
while cont <= 10:
  real = float(input('informe o {}° valor numerico real: '.format(cont)))
  soma = soma + real
  cont = cont + 1
media = soma / 10
print('A Soma dos valores informado é {} e a media é {}'.format(soma, media))