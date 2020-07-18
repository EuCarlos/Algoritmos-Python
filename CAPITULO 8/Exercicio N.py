# Elaborar um programa que leia uma matriz A de duas dimensões com sete linhas e sete colunas. Ao final apresentar o total de elementos pares existentes na matriz.
A = [[], [], [], [], [], [] ,[]]
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
print('='*70)
print('Foram digitados um total de {} numeros PARES e {} numeros IMPARES'.format(Pares, Impares))
print('='*70)
