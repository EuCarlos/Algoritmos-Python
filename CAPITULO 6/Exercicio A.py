#  Elaborar um programa que efetue a leitura de dez nomes de pessoas em uma matriz A do tipo vetor e apresenteos em seguidaloop = True
nome = []
for i in range(0, 10):
  nome.append(input("Informe o {}° nome: ".format(i)))

for x in nome:
  print("{}° nome é {}".format(nome.index(x), x))