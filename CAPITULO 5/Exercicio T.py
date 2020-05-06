# Elaborar um programa que apresente o resultado inteiro da divisão de dois números quaisquer, representando o dividendo e o divisor da divisão a ser processada. Sugestão: para a elaboração do programa, não utilize o operador aritmético de divisão com quociente inteiro DIV. Use uma solução baseada em laço. O programa deve apresentar como resultado (quociente) quantas vezes o divisor cabe no dividendo .
num1 = int(input('informe o dividendo: '))
num2 = int(input('informe o divisor: '))
quoc = 0
while num2 <= num1:
  num1 = num1 - num2
  quoc = quoc + 1
print('quociente igual a {}'.format(quoc))