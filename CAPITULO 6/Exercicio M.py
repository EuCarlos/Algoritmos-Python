#  Construir um programa que calcule a tabuada de um valor qualquer de 1 até 10 e armazene os resultados em uma matriz A de uma dimensão. Apresentar os elementos da matriz A. 
A = []
tabuada = int(input('Informe uma Tabuada: '))
for i in range(0, 11):
    A.append(i * tabuada)
for i in range(0, 11):
    print('{} x {} = A[{}]'.format(tabuada, i, A[i]))