# Escrever um programa que apresente como resultado a potência de uma base qualquer elevada a um expoente qualquer, ou seja, de BE, em que B é o valor da base e E o valor do expoente. Considere apenas a entrada de valores inteiros e positivos, ou seja, de valores naturais. Sugestão: não utilize o formato "base j expoente", pois é uma solução muito trivial. Use a técnica de laço, em que o valor da base deve ser multiplicado o número de vezes determinado no expoente . 
B = int(input('Informe o valor da Base: '))
E = int(input('Informe o valor do Expoente: '))
Cont = 1
Pont = 1
while Cont <= E:
  Pont = Pont * B
  Cont = Cont + 1
print(Pont)