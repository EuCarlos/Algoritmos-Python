# Escrever um programa que apresente os valores da sequência numérica de Fibonacci até o décimo quinto termo. A sequência de Fibonacci é formada por O, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, ... etc., obtendo-se o próximo termo a partir da soma do termo atual com o anterior sucessivamente até o infinito, se a sequência não for interrompida. Utilize para este exercício as variáveis ATUAL, ANTERIOR e PRÓXIMO. 
fib = 1
cont = 1
aux1 = 0
while cont <= 15:
  print(fib)
  aux2 = fib + aux1
  aux1 = fib
  fib = aux2  
  cont = cont + 1