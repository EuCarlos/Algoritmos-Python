# Efetuar a leitura de três valores numéricos (representados pelas variáveis A, B e C) e processar o cálculo da equação completa de segundo grau, utilizando a fórmula de Bhaskara (considerar para a solução do problema todas as possíveis condições para delta: delta < O - não há solução real, delta> O - há duas soluções reais e diferentes e delta= O - há apenas uma solução real). Lembre-se de que é completa a equação de segundo grau que possui todos os coeficientes A, B e C diferentes de zero. O programa deve apresentar respostas para todas as condições estabelecidas para delta. 
from math import sqrt
A = int(input('informe valor de A: '))
B = int(input('informe valor de B: '))
C = int(input('informe valor de C: '))
delta = (B**2) - 4 * A * C
if delta < 0:
  print('Não há solução real')
else:
  if delta == 0:
    Rr1 = -B / 2 * A
    print('Raiz Real unica: {}'.format(Rr1))
  else:
   if delta > 0:
      Rr1 = (-b + sqrt(delta))/ (2 * A)
      Rr2 = (-b - sqrt(delta))/ (2 * A)
      print('Duas raízes reais e distintas: ')
      print(' 1°Raiz Real = {} \n 2°Raiz Real = {}'.format(Rr1, Rr2))