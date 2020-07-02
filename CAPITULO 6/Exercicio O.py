#  Escrever um programa que leia 25 elementos (valores reais) para temperaturas em graus Celsius e armazene esses valores em uma matriz A de uma dimensão do tipo vetor. Construir uma matriz B de mesmo tipo e dimensão, em que cada elemento da matriz B deve ser a conversão da temperatura em graus Fahrenheit do elemento correspondente da matriz A. Apresentar os elementos das matrizes A e B. 
A = []
B = []
for i in range(0, 25):
    A.append(float(input('Informe o {}° Valor em graus Celsius no vetor A: '.format(i + 1))))
for i in range(0, 25):
    B.append(A[i] * 1.8 + 32)
for i in range(0, 25):
    print('A[{}] = {}°C é igual a B[{}] = {}°F'.format(i, A[i], i, B[i]))