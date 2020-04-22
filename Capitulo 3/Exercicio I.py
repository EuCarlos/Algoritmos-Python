# Elaborar um programa que apresente o valor da conversão em real (R$) de um valor lido em dólar(US$). O programa deve solicitar o valor da cotação do dólar e também a quantidade de dólares disponível com o usuário. 
# Elaborar um programa que apresente o valor da conversão em dólar (US$) de um valor lido em real(R$). O programa deve solicitar o valor da cotação do dólar e também a quantidade de reais disponível com o usuário. 
real = float(input('Informe em dollar para converter em real: '))
dollar = real / 5.31
print('R${} pode ser convertido para US${:.2f}'.format(real, dollar)