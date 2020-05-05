# Elaborar um programa que leia quinze valores numéricos inteiros e no final apresente o somatório da fatorial de cada valor lido. 
soma = 0
cont = 1   
while cont <= 15:
  num = int(input('Informe o numero: '))
  fat = 1
  aux = 1
  while aux <= num:
    fat = fat * aux
    aux = aux + 1
  soma = soma + fat
  cont = cont + 1
print(soma)