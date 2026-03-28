print('{:-^40}'.format(' 10 Termos de uma PA '))
num1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
decimo = num1 + (10 - 1) * razao
print('-=-' * 25)
for c in range(num1, decimo + razao, razao):
    print(c, end=' - ')
print('ACABOU')
print('-=-' * 25)

# OU
# pt = int(input('Primeiro Termo: '))
# r = int(input('Razão: '))
# for n in range(1, 11):
#    pa = pt + (n - 1) * r
#    print(f'o {n}° termo da pa é {pa}')