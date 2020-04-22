# Elaborar um programa que apresente o valor da conversão em real (R$) de um valor lido em dólar(US$). O programa deve solicitar o valor da cotação do dólar e também a quantidade de dólares disponível com o usuário. 
dollar = float(input('Informe em dollar para converter em real: '))
real = dollar * 5.31
print('US${} pode ser convertido para R${}'.format(dollar, real))