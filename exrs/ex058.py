# COLOCAR COR!!!
from random import choice
from time import sleep
# from random import randint(escolhe o número já)
# escolhido = randint(0, 5)
tentativas = 1
print('-=-' * 25)
print('Em uma lista de 1 a 10, escolha um número, se você acertar, venceu!')
print('-=-' * 25)
lista = [1,2,3,4,5,6,7,8,9,10]
sorteado = choice(lista)
escolhido = int(input('Digite o número que você escolheu: '))
print('Processando...')
sleep(1)
while escolhido != sorteado:
    tentativas += 1
    if escolhido > sorteado:
        print('Menos... Tente mais uma vez!')
        escolhido = int(input('Qual é seu novo palpite? '))
    else:
        print('Mais... Tente mais uma vez!')
        escolhido = int(input('Qual é seu novo palpite? '))
print('- * -' * 10)
if tentativas == 1:
    print(f'O número sorteado foi {sorteado}. Parabéns, você acertou com {tentativas} tentativa!')
else:
    print(f'O número sorteado foi {sorteado}. Parabéns, você acertou com {tentativas} tentativas!')
print('- * -' * 10)