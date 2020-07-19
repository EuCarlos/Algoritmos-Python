#  Elaborar um programa que leia duas matrizes A e B, cada uma de duas dimensões com cinco linhas e seis colunas. A matriz A deve aceitar a entrada de valores pares, enquanto a matriz B deve aceitar a entrada de valores ímpares. As entradas dos valores nas matrizes A e B devem ser validadas pelo programa e não pelo usuário. Construir a matriz C de mesma dimensão, que seja formada pela soma dos elementos da matriz A com os elementos da matriz B. Apresentar os elementos da matriz C.
A = [[], [], [], [], []]
B = [[], [], [], [], []]
C = [[], [], [], [], []]
for i in range(len(A)):
    for j in range(6):
        Aux = 1
        while(Aux % 2 == 1):
            Aux = int(input('Informe um valor para a matriz A[{}][{}]: '.format(i, j)))
            if(Aux % 2 == 1):
                print('ERRO: Na matriz A só são aceitos numeros PARES')
        A[i].append(Aux)

print('='*70)
for i in range(len(B)):
    for j in range(6):
        Aux = 0
        while(Aux % 2 == 0):
            Aux = int(input('Informe um valor para a matriz B[{}][{}]: '.format(i, j)))
            if(Aux % 2 == 0):
                print('ERRO: Na matriz B só são aceitos numeros IMPARES')
        B[i].append(Aux)

for i in range(len(C)):
    for j in range(6):
        C[i].append(A[i][j] + B[i][j])

print('='*70)
for i in range(len(C)):
    for j in range(6):
        print('C[{}][{}] = {}'.format(i, j, C[i][j]))
