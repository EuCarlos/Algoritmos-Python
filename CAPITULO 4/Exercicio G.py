# Fazer a leitura de quatro valores numéricos inteiros representados pelas variáveis A, B, C e D. Apresentar apenas os valores que sejam divisíveis por 2 e 3.
A = int(input('Informe o valor de A: '))
B = int(input('Informe o valor de B: '))
C = int(input('Informe o valor de C: '))
D = int(input('Informe o valor de D: '))
if A % 2 == 0 and A % 3 == 0:
  div2A = A / 2
  div3A = A / 3
  print(' Divição por 2 de A= {} \n Divição por 3 de A = {}'.format(div2A, div3A))
if B % 2 == 0 and B % 3 == 0:
  div2B = A / 2
  div3B = A / 3
  print(' Divição por 2 de B= {} \n Divição por 3 de B = {}'.format(div2B, div3B))
if C % 2 == 0 and A % 3 == 0:
  div2C = A / 2
  div3C = A / 3
  print(' Divição por 2 de C= {} \n Divição por 3 de C = {}'.format(div2C, div3C))
if D % 2 == 0 and A % 3 == 0:
  div2D = A / 2
  div3D = A / 3
  print(' Divição por 2 de D= {} \n Divição por 3 de D = {}'.format(div2D, div3D))