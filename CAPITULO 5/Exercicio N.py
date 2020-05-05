# Elaborar um programa que leia sucessivamente valores numéricos e apresente no final o somatório, a média e o total de valores lidos. O programa deve ler os valores enquanto o usuário estiver fornecendo valores positivos. Ou seja, o programa deve parar quando o usuário fornecer um valor negativo (menor que zero). 
cont = 0
num = 0
soma = 0
while num >= 0:
  num = int(input('informe um valor positivo: '))
  soma = soma + num
  cont = cont + 1
media = soma / cont
print('Foi lido um total de {} numeros, a soma deu {}, e a media de {}'.format(cont, soma, media))