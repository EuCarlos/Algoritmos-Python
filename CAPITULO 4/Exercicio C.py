# Realizar a leitura dos valores de quatro notas escolares bimestrais de um aluno representadas pelas variáveis N1, N2, N3 e N4. Calcular a média aritmética (variável MD) desse aluno e apresentar a mensagem "Aprovado" se a média obtida for maior ou igual a 5; caso contrário, apresentar a mensagem "Reprovado". Informar também, após a apresentação das mensagens, o valor da média obtida pelo aluno.
N1 = float(input('Infomorme a 1° Nota: '))
N2 = float(input('Infomorme a 2° Nota: '))
N3 = float(input('Infomorme a 3° Nota: '))
N4 = float(input('Infomorme a 4° Nota: '))
MD = (N1 + N2 + N3 + N4)/4
if MD >= 5:
  print('Sua nota é {:.1f} | APROVADO'.format(MD))
else:
  print('Sua nota é {:.1f} | REPROVADO'.format(MD))