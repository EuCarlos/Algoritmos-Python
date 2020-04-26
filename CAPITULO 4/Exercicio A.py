#  Efetuar a leitura de dois valores numéricos inteiros representados pelas variáveis A e B e apresentar o resultado da diferença do maior valor pelo menor valor.
A = int(input('Informe valor de A: '))
B = int(input('Informe valor de B: '))
if A > B:
    print('A diferença é {}'.format(A - B))
else:
    print('A diferença é {}'.format(B - A))