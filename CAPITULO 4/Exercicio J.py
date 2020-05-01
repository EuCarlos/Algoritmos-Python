# Ler um valor numérico inteiro e apresentar uma mensagem informando se o valor fornecido é par ou ímpar.
Num = int(input('Informe um valor numerico: '))
if Num % 2 == 0:
  print('Numero {} é Par'.format(Num))
else:
  print('Numero {} é Impar'.format(Num))