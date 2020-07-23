#  Escrever um programa que leia 20 elementos numéricos inteiros negativos em uma matriz A do tipo vetor. Construir uma matriz B de mesmo tipo e dimensão, em que cada elemento deve ser o valor positivo do elemento correspondente da matriz A. Desta forma, se em A[1] estiver armazenado o elemento -3, deve estar em B[1] o valor 3, e assim por diante. Apresentar os elementos da matriz B em ordem decrescente.
A = []
B = []
for i in range(20):
    Aux = 1
    while(Aux > 0):
        Aux = int(input('Informe um valor para a matriz A[{}]: '.format(i)))
        if(Aux > 0):
            print('Por favor, informe um numero negativo!')
    A.append(Aux)
for i in range(20):
    B.append(A[i] * -1)
B = sorted(B)
B.sort(reverse = True)

for i in range(20)
    print(B[i])
