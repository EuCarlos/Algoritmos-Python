# Construir um programa que apresente a soma dos cem primeiros números naturais (1+2+3+ ... +98+99+100). 
Cont = 1
Soma = 0
while Cont <= 100:
  Soma = Soma + Cont
  Cont = Cont + 1
print('Resultado da soma dos numero é {}'.format(Soma))