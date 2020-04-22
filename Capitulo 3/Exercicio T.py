# Construir um programa que calcule e apresente em metros por segundo o valor da velocidade de um projétil que percorre uma distância em quilômetros a um espaço de tempo em minutos. Utilize a fórmula VELOCIDADE <- (DISTÂNCIA* 1000) /(TEMPO* 60).
dist = int(input('informe a distancia: '))
tmp = int(input('informe o tempo: '))
vel = (dist * 1000)/(tmp * 60)
print('A velocidade percorrida do projetil é igual a {}m/s'.format(vel))