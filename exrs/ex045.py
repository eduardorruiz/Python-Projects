from time import sleep
from random import randint
print('{:-^50}'.format(' JOGO PEDRA, PAPEL E TESOURA! '))
lista = ('Pedra', 'Papel', 'Tesoura')
escolhacomputador = randint(0, 2)
print('Escolha entre Pedra, Papel ou Tesoura.')
escolha = input('Sua escolha é: ').strip().capitalize()
print('1', end='')
sleep(1)
print(', 2', end='')
sleep(1)
print(' e 3.')
sleep(0.8)
print('JO-KEN-PÔ!!')
sleep(0.5)
print(f'O computador escolheu \033[1m{lista[escolhacomputador]}\033[m', end=' ')
print(f'e você \033[1m{escolha}\033[m.')
print('--=--' * 15)
print(' ')
if escolhacomputador == 0: # PEDRA
    if escolha == 'Pedra':
        print('EMPATOU!!!')
    elif escolha == 'Papel':
        print('Você venceu, PARÁBENS!!!')
    elif escolha == 'Tesoura':
        print('Você perdeu, tente novamente!!')
    else:
        print('JOGADA INVÁLIDA!')
elif escolhacomputador == 1: # PAPEL
    if escolha == 'Pedra':
        print('Você perdeu, tente novamente!!')
    elif escolha == 'Papel':
        print('EMPATOU!!!')
    elif escolha == 'Tesoura':
        print('Você ganhou, PARÁBENS!!!')
    else:
        print('JOGADA INVÁLIDA!')
elif escolhacomputador == 2: # TESOURA
    if escolha == 'Pedra':
        print('Você ganhou, PARÁBENS!!!')
    elif escolha == 'Papel':
        print('Você perdeu, tente noovamente!!')
    elif escolha == 'Tesoura':
        print('EMPATOU!!!')
    else:
        print('JOGADA INVÁLIDA!')
print(' ')
print('--=--' * 15)
