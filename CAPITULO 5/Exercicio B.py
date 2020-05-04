# Elaborar um programa que mostre os resultados da tabuada de um número qualquer, a qual deve ser apresentada de acordo com sua forma tradicional. 
Tab = int(input('Informe uma tabuada: '))
n = 0
while n <= 10:
  rslt = Tab * n
  print('{} x {} = {}'.format(Tab, n, rslt))
  n = n + 1