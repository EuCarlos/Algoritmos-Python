# Construir um programa que apresente como resultado a fatorial dos valores ímpares situados na faixa numérica de 1 até 1 O. 
fat = 1
cont = 1
while cont <= 10:
  r = cont - 2 * (cont / 2)
  if r != 0:
    fat = 1
    aux = 1
    while aux <= cont:
      fat = fat * aux
      aux = aux + 1
    print(fat)
  cont = cont + 1