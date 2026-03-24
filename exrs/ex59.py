from time import sleep
print('-=-' * 12)
print('PROGRAMA COM UM MENU DE OPÇÕES')
print('-=-' * 12)
n1 = int(input('Digite o primeiro valor:'))
n2 = int(input('Digite o segundo valor:'))
opção = 0
# PODERIA COLOCAR ESSA SOMA, MULTI E MAIOR DENTRO DO IF E ELIF!
soma = n1 + n2
multiplicar = n1 * n2
if n1 > n2:
    maior = n1
else:
    maior = n2
while opção != 5:
    print('-*-' * 12)
    print('     [1] somar\n     [2] multiplicar\n     [3] maior\n     [4] novos números\n     [5] sair do programa')
    print('-*-' * 12)
    opção = int(input('Qual é sua opção: '))
    print('- - ' * 5)
    if opção == 1:
        print(f'A soma entre {n1} + {n2} = {soma}')
    elif opção == 2:
        print(f'A multiplicação entre {n1} x {n2} = {multiplicar}')
    elif opção == 3:
        print(f'Entre [{n1}] e [{n2}] o maior é [{maior}]')
    elif opção == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        soma = n1 + n2
        multiplicar = n1 * n2
        maior = n1 if n1 > n2 else n2
    else:
        print('Opção invalida! Tente novamente.')
print('Finalizando...')
sleep(2.3)
print('-*-' * 12)
print('FIM DO PROGRAMA')

