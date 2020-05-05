# Escrever um programa que calcule e apresente o somatório do número de grãos de trigo que se pode obter num tabuleiro de xadrez, obedecendo à seguinte regra: colocar um grão de trigo no primeiro quadro e nos quadros seguintes o dobro do quadro anterior. Ou seja, no primeiro quadro coloca-se um grão, no segundo quadro colocam-se dois grãos (neste momento, tem-se três grãos), no terceiro quadro colocam-se quatro grãos (tendo neste momento sete grãos), no quarto quadro colocam-se oito grãos (tendo-se então 15 grãos) até atingir o sexagésimo quarto quadro (este exercício foi baseado numa situação exposta no capítulo 16 do livro "O Homem que Calculava" de Malba Tahan, da Editora Record). 
grao = 0
quadro = 1
cont = 1
while cont <= 64:
  grao = grao + quadro
  quadro = quadro * 2
  cont = cont + 1
print(grao)