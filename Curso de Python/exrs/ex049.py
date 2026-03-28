print('{:-^45}'.format(' PROGRAMA DE TABUADA '))
n = int(input('Digite o número que você quer ver a tabuada: '))
print('-=-' * 15)
for cont in range(1,11):
    print(f'{n} X {cont} = {n * cont}')
print('-=-' * 15)