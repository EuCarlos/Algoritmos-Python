# Ler os valores de quatro notas escolares bimestrais de um aluno representadas pelas variáveis N1, N2, N3 e N4.Calcular a média aritmética (variável MD1) desse aluno e apresentar a mensagem "Aprovado" se a média obtida for maior ou igual a 7; caso contrário, o programa deve solicitar a quinta nota (nota de exame, representada pela variável NE) do aluno e calcular uma nova média aritmética (variável MD2) entre a nota de exame e a primeira média aritmética. Se o valor da nova média for maior ou igual a cinco, apresentar a mensagem "Aprovado em exame"; caso contrário, apresentar a mensagem "Reprovado". Informar também, após a apresentação das mensagens, o valor da média obtida pelo aluno
N1 = float(input('Infomorme a 1° Nota: '))
N2 = float(input('Infomorme a 2° Nota: '))
N3 = float(input('Infomorme a 3° Nota: '))
N4 = float(input('Infomorme a 4° Nota: '))
MD = (N1 + N2 + N3 + N4)/4
if MD >= 5:
  print('Sua nota é {:.1f} | APROVADO'.format(MD))
else:
  NE = float(input('informe a Nota do Exame: '))
  MD2 = (N1 + N2 + N3 + N4 + NE)/5
  if MD2 >= 5:
    print('Sua nota é {:.1f} | APROVADO EM EXAME'.format(MD2))
  else:
    print('Sua nota é {:.1f} | REPROVADO'.format(MD2))