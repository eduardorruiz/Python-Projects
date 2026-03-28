from random import choice

print('-*-' * 6)
print('PAR ou ÍMPAR GAME')
print('-*-' * 6)

from random import choice
lista = [1,2,3,4,5,6,7,8,9,10]
soma = vitoria = 0
while True:
    valor = int(input('Diga seu valor: '))
    pi = str(input('Par ou Ímpar [P/I]: ')).strip().upper()[0]
    computador = choice(lista)
    soma = valor + computador
    if pi == 'P':
        if soma % 2 == 0:
            print(f'Você GANHOU')
            print(f'Você escolheu {valor} e o computador escolheu {computador}, total de {soma} --> DEU PAR')
            print('- - ' * 14)
        else:
            print(' - - - GAME OVER - - - ')
            print(f' Você venceu {vitoria} vezes até perder')
            break
    if pi == 'I':
        if soma % 2 == 0:
            print(' - - - GAME OVER - - - ')
            print(f' Você venceu {vitoria} vezes até perder')
            break
        else:
            print('Você GANHOU')
            print(f'Você escolheu {valor} e o computador escolheu {computador}, total de {soma} --> DEU ÍMPAR')
            print('- - ' * 14)
    vitoria += 1
