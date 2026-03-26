""" Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para
cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.  """

n = 0
cont = 1
while True:
    cont = 1
    print('-*-' * 10)
    n = int(input('Quer ver a tabuada de qual valor: '))
    print('-*-' * 10)
    if n < 0:
        break
    while cont <= 10:
    # for c in range(1,11):
        print(f'{n} x {cont} = {n * cont} ')
        cont += 1