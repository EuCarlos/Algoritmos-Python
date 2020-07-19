#  Elaborar um programa que leia uma matriz A de duas dimensões com dez linhas e sete colunas. Ao final apresentar o total de elementos pares e ímpares existentes na matriz. Apresentar também o percentual de elementos pares e ímpares em relação ao total de elementos da matriz. Supondo a existência de 20 elementos pares e 50 elementos ímpares, ter-se-ia 28,6°/o de elementos pares e 71,4o/o de elementos ímpares.
A = [[], [], [], [], [], [] ,[], [], [], []]
Pares = 0
Impares = 0
for i in range(len(A)):
    for j in range(7):
        A[i].append(int(input('Informe um valor para A[{}][{}]: '.format(i, j))))
for i in range(len(A)):
    for j in range(7):
        if(A[i][j] % 2 == 0):
            Pares += 1
        else:
            Impares += 1
PercentPares = (Pares * 100) / 70
PercentImpares = (Impares * 100) / 70
print('='*70)
print('Foram digitados um total de {} numeros PARES e {} numeros IMPARES'.format(Pares, Impares))
print('Com {}% de numeros PARES e {}% de numeros IMPARES'.format(PercentPares, PercentImpares))
print('='*70)
