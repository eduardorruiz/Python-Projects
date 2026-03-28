from time import sleep
print('-=-' * 30)
vel = int(input('Digite a velocidade que seu carro estava: '))
print('-=-' * 30)
if vel > 80 :
    print('MULTADO! você excedeu o limite de velocidade de 80 km/h ')
    print('segue abaixo a taxa que deve ser paga!')
    multa = (vel - 80) * 7
    sleep(1)
    print(f'A taxa a ser paga é de {multa} reais.')
else:
    print('A velocidade estava adequada, Bom Dia motorista!')

