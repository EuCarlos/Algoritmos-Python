# Construir um programa que leia um valor numérico inteiro e apresente como resultado os seus valores sucessor e antecessor. 
num = int(input('informe um valor numerico: '))
suc = num + 1
ant = num - 1
print('antecessor =  {} \nsucessor = {}'.format(ant, suc))