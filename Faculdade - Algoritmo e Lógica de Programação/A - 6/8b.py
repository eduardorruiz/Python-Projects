# Adicionar condições para o laço de teste rodar menos vezes

n = int(input('Digite um número: '))
cont = 1
total = 0
while cont <= n:
    if n % cont == 0:
        total += 1
    cont += 1
if total == 2:
    print(f'\nO número [{n}] é primo!')
else:
    print(f'\nO número [{n}] não é primo!')
print('\nFim do Programa')
