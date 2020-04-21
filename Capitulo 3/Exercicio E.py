# Efetuar o cálculo e apresentar o valor de uma prestação de um bem em atraso, utilizando a fórmula PRESTAÇÃO <- VALOR+ (VALOR* (TAXA/100) * TEMPO). 
vlr = float(input('informe o valor da prestação: '))
tx = float(input('informe a taxa: '))
tmp = int(input('informe o tempo: '))
prst = vlr + (vlr * (tx / 100)* tmp)
print('O atual da prestação é {}'.format(prst))