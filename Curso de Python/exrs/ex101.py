""" Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai
receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal
indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições."""

def voto():
    from datetime import date
    ano = date.today().year
    nascimento = int(input('Digite o ano que você nasceu: '))
    idade = ano - nascimento
    if idade < 16:
        resposta = f'Com {idade} anos não vota, NEGADO!'
    elif 16 <= idade <= 18 or idade > 65:
        resposta = f'Com {idade} anos pode votar, OPCIONAL!'
    else:
        resposta = f'Com {idade} anos deve votar, OBRIGATÓRIO!'
    return resposta
print(voto())