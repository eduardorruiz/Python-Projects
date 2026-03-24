from random import choice
from time import sleep
# from random import randint(escolhe o número já)
# escolhido = randint(0, 5)
print('-=-' * 25)
print('Em uma lista de 1 a 5, escolha um número, se você acertar, venceu!')
print('-=-' * 25)
lista = [1,2,3,4,5]
sorteado = choice(lista)
escolhido = int(input('Digite o número que você escolheu: '))
print('Processando...')
sleep(1.5)
if escolhido == sorteado:
    print(f'O número sorteado foi {sorteado}. Parabéns, você acertou!')
else:
    print(f'O número sorteado foi {sorteado} e não {escolhido}. Perdeu!\n')
print('Jogue novamente, quando puder!!')
