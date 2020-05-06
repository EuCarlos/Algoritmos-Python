# Escrever um programa que possibilite calcular a área total em metros de uma residência com os cômodos sala, cozinha, banheiro, dois quartos, área de serviço, quintal, garagem, entre outros, que podem ser fornecidos ao programa. O programa deve solicitar a entrada do nome, da largura e do comprimento de um determinado cômodo. Em seguida, deve apresentar a área do cômodo lido e também uma mensagem solicitando ao usuário a confirmação de continuar calculando novos cômodos. Caso o usuário responda "NÃO", o programa deve apresentar o valor total acumulado da área residencial. 
resp = 'S'
while resp == 'S':
  comodo = input('informe o comodo: ')
  larg = float(input('Informe a largura do comodo: '))
  cmpr = float(input('Informe o comprimento do comodo: '))
  area = larg * cmpr
  print('A area da(o){} é {}²'.format(comodo, area))
  print('================================================')
  resp = input('deseja continuar? [S/N]: ')
print  ('-------------- FINAL DO PROCESSO ---------------')