# Elaborar um programa que apresente os resultados da soma e da média aritmética dos valores pares situados na faixa numérica de 50 até 70. 
cont = 50
soma = 0
QuantPares = 0
while cont <= 70:
  if cont % 2 == 0:
    soma = soma + cont
    QuantPares = QuantPares + 1
  cont = cont + 1
media = soma / QuantPares
print('Total de {} numeros pare somados que o resultado é {}, com a media de {}'.format(QuantPares, soma, media))