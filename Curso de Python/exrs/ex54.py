from datetime import date
cont1 = 0
cont2 = 0
for c in range(1, 7):
    nascimento = int(input(f'Digite o ano que a {c}° pessoa nasceu: '))
    anoatual = date.today().year
    idade = anoatual - nascimento
    if idade >= 18:
        cont1 += 1
    else:
        cont2 += 1
if cont1 != 1: # != significa diferente de
    print(f'Ao todo tivemos {cont1} adultos com mais de 18 anos.')
else:
    print(f'Ao todo tivemos {cont1} adulto com mais de 18 anos.')
if cont2 != 1:
    print(f'E também tivemos {cont2} jovens com mais de 18 anos.')
else:
    print(f'E também tivemos {cont2} jovem com mais de 18 anos.')
