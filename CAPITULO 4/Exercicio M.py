# Efetuar a leitura de um nome (variável NOME) e o sexo (variável SEXO) de uma pessoa e apresentar como saída uma das seguintes mensagens: "llmo. Sr.", caso seja informado o sexo masculino (utilizar como valor o caractere "M"), ou "llma. Sra.", caso seja informado o sexo feminino (utilizar como valor o caractere "F"). Após a mensagem de saudação, apresentar o nome informado. O programa deve, após a entrada do sexo, verificar primeiramente se o sexo fornecido é realmente válido, ou seja, se é igual a "M" ou a "F". Não sendo essa condição verdadeira, o programa deve apresentar a mensagem "Sexo informado inválido". 
Nome = input('Informe o Nome: ')
Sexo = input('Informe o sexo [F/M]: ')
if Sexo == 'M':
  print('llmo. Sr. {}'.format(Nome))
else:
  if Sexo == 'F':
    print('llma. Sra. {}'.format(Nome))
  else:
    print('Sexo informado inválido.')