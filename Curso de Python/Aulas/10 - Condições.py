# Exercicio de Condicionais --> 28 a 35
#if carro.esquerda():
 #   bloco.True
#else:
 #   bloco.False

tempo = int(input('Quantos anos tem seu carro?'))
if tempo <=3:
    print('Carro novo.')
else:
    print('Carro velho.')
print('Fim.')

# OU A CONDIÇÃO SIMPLIFICADA:

#tempo = int(input('Quantos anos tem seu carro?'))
#print('Carro novo'if tempo<=3 else 'carro velho')
#print('Fim.')

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
md = (n1 + n2) / 2
if md >=7:
    print(f'Parabéns você passou com {md}, agora boas férias!')
else:
    print(f'Infelizmente ficou de recuperação, pois sua média foi de {md}, estude um pouco mais!')
print('See you later student')