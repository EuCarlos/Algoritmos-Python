# Elaborar um programa que apresente o somatório dos valores pares existentes na faixa de 1 até 500.
Cont = 1
Soma = 0
while Cont <= 500:
  if Cont % 2 == 0:
    Soma = Soma + Cont
  Cont = Cont + 1
print('Somatorio dos numeros pares ate 500 é {}'.format(Soma))