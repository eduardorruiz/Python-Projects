nascimento = int(input('A Confederação Nacional de Natação precisa do seu ano de nascimento para determinar sua categoria, indique-o aqui: '))
from datetime import date
atual = date.today().year
idade = atual - nascimento
print(f'Com os seus {idade} anos,', end=' ')
if 0 < idade <= 9:
    print('você está no MIRIM!!')
elif 9 < idade <= 14:
    print('você está no INFANTIL!!')
elif 14 < idade <= 19:
    print('você está no JUNIOR!!')
elif 19 < idade <= 25:
    print('você está no SÊNIOR!!')
elif idade > 25:
    print('parábens, você está no MASTER!!')
else:
    print(' ERRO!')
