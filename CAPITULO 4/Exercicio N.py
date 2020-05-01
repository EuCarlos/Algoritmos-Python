# Efetuar a leitura de três valores inteiros desconhecidos representados pelas variáveis A, B e C. Somar os valores fornecidos e apresentar o resultado somente se for maior ou igual a 100. 
A = int(input('Informe valor de A: '))
B = int(input('Informe valor de B: '))
C = int(input('Informe valor de C: '))
Soma = A + B + C
if Soma >= 100:
  print(Soma)