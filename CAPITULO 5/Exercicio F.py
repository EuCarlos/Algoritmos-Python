# Construir um programa que apresente todos os valores numéricos divisíveis por 4 e menores que 200. Sugestão: a variável que controla o contador do laço deve ser iniciada com valor 1. 
Cont = 1
while Cont < 200:
  if Cont % 4 == 0:
    print(Cont)
  Cont = Cont + 1