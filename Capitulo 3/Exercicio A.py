# Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit. A fórmula de conversão é F = (9 * C + 160) / 5, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius. 
C = int(input('Informe o valor de em °C: '))
F = (9 * C + 160)/5
print('{}°C é equivalente a {}°F'.format(C , F))