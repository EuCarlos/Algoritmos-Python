# Efetuar a leitura de um valor numérico inteiro positivo ou negativo representado pela variável N e apresentar o valor lido como sendo positivo. Dica: se o valor lido for menor que zero, ele deve ser multiplicado por -1. 
N = int(input('informe um numero: '))
if N <= 0:
  N = N * -1
  print('Numero Positivo é: {}'.format(N))
else:
  print('Numero Positivo é: {}'.format(N))