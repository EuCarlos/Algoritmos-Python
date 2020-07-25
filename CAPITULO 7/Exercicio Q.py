#  Elaborar um programa que leia dez elementos do tipo cadeia em uma matriz A e apresentá-los utilizando pesquisa binária.
A = []
for i in range(15):
    A.append(str(input('Informe um valor para a Matriz A[{}]'.format(i))))

for i in range(14):
    for j in range(i + 1, 15):
        if (A[i] > A[j]):
            x = A[i]
            A[i] = A[j]
            A[j] = x

R = 'SIM'
while( R == 'SIM'):
    Pesq = float(input('Pesquisa: '))
    Inicio = 1
    Fim = 15
    Acha = False
    while((Inicio <= Fim) and (Acha == False)):
        Meio = (Inicio + Fim) / 2
        if (Pesq == A[Meio]):
            Acha = True
        else:
            if(Pesq < A[Meio]):
                Fim = Meio - 1
            else:
                Inicio = Meio + 1
    if(Acha == True):
        print('{} foi localizado na posição {}'.format(Pesq, Meio))
    else:
        print('{} não foi localizado'.format(Pesq))
    R = input('Resp: ')
