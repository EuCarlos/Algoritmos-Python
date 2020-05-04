# Elaborar um programa que apresente os valores de conversão de graus Celsius em graus Fahrenheit, de dez em dez graus, iniciando a contagem em dez graus Celsius e finalizando em cem graus Celsius. O programa deve apresentar os valores das duas temperaturas.
cont = 0
while cont <= 100:
  Fahr = (9 * cont + 160)/5
  print('{}°C é equivalente a {}°F'.format(cont, Fahr))
  cont = cont + 10