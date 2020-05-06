# Elaborar um programa que leia valores positivos inteiros até que um valor negativo seja informado. Ao final devem ser apresentados o maior e o menor valores informados pelo usuário. 
num = 0
numMaior = 0
numMenor = 0
while num >= 0:
  if num > numMaior:
    numMaior = num
  if num < numMenor:
    numMenor = num
  num = int(input('informe valores positivos: '))
print('O Maior numero é {} e o Menor numero é {}'.format(numMaior, numMenor))