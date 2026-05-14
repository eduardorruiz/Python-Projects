"""O programa deverá ler dois inteiros chamados Min e Max. Min pode ser qualquer valor e Max, obrigatoriamente,
deve ser maior que Min. Em seguida preencher a lista com todos os valores situados entre Min e Max que sejam
divisíveis por 7. Exibir a lista resultante na tela."""

min = int(input('Digite seu valor mínimo: '))
max = int(input('Digite seu valor máximo: '))
while min > max:
    print('Erro, seu valor mínimo é maior que seu valor máximo.')
    max = int(input('Porfavor, digite um valor máximo válido: '))
list = []
for num in range(min, max):
    if num % 7 == 0:
        list.append(num)
print(f'A lista resultante é {list}')
