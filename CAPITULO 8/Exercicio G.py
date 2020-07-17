#  Elaborar um programa que leia uma matriz A de duas dimensões com quatro linhas e cinco colunas, armazenando nessa matriz os valores das temperaturas em graus Celsius. Construir a matriz 8 de mesma dimensão, em que cada elemento seja o valor da temperatura em graus Fahrenheit de cada elemento correspondente da matriz A. Apresentar ao final as matrizes A e B
A = [[], [], [], []]
B = [[], [], [], []]
for i in range(len(A)):
    for j in range(5):
        A[i].append(float(input('Informe um valor em °C para a matriz A: ')))
for i in range(len(B)):
    for j in range(5):
        fahr = (A[i][j] * 1.8) + 32
        B[i].append(fahr)
print('='*60)
for i in range(len(B)):
    for j in range(5):
        print('A[{}][{}] = {}°C é igual a B[{}][{}] = {}°F'.format(i, j, A[i][j], i, j, B[i][j]))
