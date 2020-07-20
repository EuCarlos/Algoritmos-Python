#  Elaborar um programa que leia duas matrizes A e B de duas dimensões com quatro linhas e cinco colunas.A matriz A deve ser formada por valores divisíveis por 3 e 4, enquanto a matriz B deve ser formada por valores divisíveis por 5 ou 6. As entradas dos valores nas matrizes devem ser validadas pelo programa e não pelo usuário. Construir e apresentar a matriz C de mesma dimensão e número de elementos que contenha a subtração dos elementos da matriz A em relação aos elementos da matriz B
A = [[], [], [], []]
B = [[], [], [], []]
B = [[], [], [], []]
for i in range(len(A)):
    for j in range(5):
        Aux = 1
        while(not(Aux % 3 == 0) and not(Aux % 4 == 0)):
            Aux = int(input('Informe um valor para a matriz A[{}][{}]: '.format(i, j)))
            if(Aux % 2 == 1):
                print('ERRO: Na matriz A só são aceitos numeros Divisieis por 3 e 4.')
        A[i].append(Aux)
for i in range(len(B)):
    for j in range(5):
        Aux = 1
        while(not(Aux % 5 == 0) and not(Aux % 6 == 0)):
            Aux = int(input('Informe um valor para a matriz B[{}][{}]: '.format(i, j)))
            if(Aux % 2 == 1):
                print('ERRO: Na matriz A só são aceitos numeros Divisieis por 5 e 6.')
        B[i].append(Aux)

for i in range(len(C)):
    for j in range(5):
        C[i].append(A[i][j] - B[i][j])

print('='*70)
for i in range(len(C)):
    for j in range(5):
        print(C[i][j])
