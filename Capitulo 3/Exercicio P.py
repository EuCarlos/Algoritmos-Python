# Elaborar um programa que leia o valor numérico correspondente ao salário mensal (variável SM) de um trabalhador e também faça a leitura do valor do percentual de reajuste (variável PR) a ser atribuído. Apresentar o valor do novo salário (variável NS). 
SM = int(input('Salarios Mensal: '))
PR = int(input('Perecentual de Reajuste: '))
NS = (PR / 100 * SM) + SM
print('Novo Salario: {}'.format(NS))