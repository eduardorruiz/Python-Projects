from datetime import date
print('Olá, neste programa você saberá sobre a data do seu alistamento militar.')
nascimento = int(input('Seu ano de nascimento: '))
atual = date.today().year
idade = atual - nascimento
print(f'Quem nasceu em \033[4m{nascimento}\033[m tem \033[1m{idade} anos\033[m em \033[4m{atual}\033[m')
if idade == 18:
    print('Este é o ano do seu alistamento rapaz!')
elif idade > 18:
    saldo = idade - 18
    foi = atual - saldo
    print('O tempo de você se alistar já passou.')
    print(f'Seu alistamento foi há {saldo} anos.\nSeu alistamento foi em {foi}.')
else:
    saldo = 18 - idade
    sera = atual + saldo
    print(f'Ainda faltam {saldo} anos para seu alistamento, será apenas em {sera}.')