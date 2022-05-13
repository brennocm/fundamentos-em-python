a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

# soma = str(soma)
# subtracao = str(subtracao)
# multiplicacao = str(multiplicacao)
# divisao = str(divisao)
# resto = str(resto)

print ('Os números analisados são: ' + str(a) + ' e ' + str(b))

# print('soma ' + str(soma))
print('soma {} \nsubtracao {} \nmultipiplicacao {} \ndivisao {} \nresto {}' .format(soma, subtracao, multiplicacao, divisao, resto))

# print('subtracao ' + str(subtracao))
# print('multiplicacao ' + str(multiplicacao))
# print('divisao ' + str(divisao))
# print('resto ' + str(resto))
