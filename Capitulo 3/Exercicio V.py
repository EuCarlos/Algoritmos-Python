# Elaborar um programa que leia dois valores numéricos inteiros, os quais devem representar a base e o expoente de uma potência, calcule a potência e apresente o resultado obtido. 
Base = int(input('Informe o valor da base: '))
Exp = int(input('Informe o do expoente: '))
rest = Base ** Exp
print('A portencia das valores digitados é {}'.format(rest))