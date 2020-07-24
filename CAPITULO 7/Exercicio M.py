# Elaborar um programa que leia duas matrizes A e B de uma dimensão do tipo vetor com 12 elementos reais cada. Construir uma matriz C de mesmo tipo e dimensão que seja formada pelo produto de cada elemento correspondente às matrizes A e B. Montar o trecho de pesquisa sequencial para pesquisar os elementos existentes na matriz C.
A = []
B = []
C = []
for i in range(12):
    A.append(float(input('Informe um valor para a matriz A[{}]: '.format(i))))
for i in range(12):
    B.append(float(input('Informe um valor para a matriz B[{}]: '.format(i))))
for i in range(12):
    C.append(A[i] * B[i])

R = "SIM"
while(R == "SIM"):
    Pesq = int(input('Pesquisa'))
    i = 1
    Acha = False
    while((i <= 12) and (Acha ==  False)):
        if(Pesq == C[i]):
            Acha = True
        else:
            i += 1
    if(Acha == True):
        print('{} foi localizado na posição {}'.format(Pesq, i))
    else:
        print('{} não foi encontrado.'.format(Pesq))
    R = input('RESPOSTA: ')
