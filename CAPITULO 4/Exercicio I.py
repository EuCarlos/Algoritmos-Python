# Ler cinco valores numéricos inteiros (variáveis A, B, C, D e E), identificar e apresentar o maior e o menor valores informados. Não execute a ordenação dos valores como no exercício "f'.
A = int(input('Informe valor de A: '))
B = int(input('Informe valor de B: '))
C = int(input('Informe valor de C: '))
D = int(input('Informe valor de D: '))
E = int(input('Informe valor de E: '))
VMaior = A
if VMaior < B:
  VMaior = B
if VMaior < C:
  VMaior = C
if VMaior < D:
  VMaior = D
if VMaior < E:
  VMaior = E
VMenor = A
if VMenor > B:
  VMenor = B
if VMenor > C:
  VMenor = C
if VMenor > D:
  VMenor = D
if VMenor > E:
  VMenor = E
print('Valor Maior = {} \nValorMenor = {}'.format(VMaior, VMenor))