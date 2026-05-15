""" Utilize uma lista para resolver o problema a seguir. Uma empresa paga a seus vendedores um valor fixo mais comissão.
O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um
vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um
total de $470. Escreva um programa que leia contenha um laço no qual será feita a leitura do valor bruto de cada
vendedor e o cálculo do total, enquadrando-o em uma das faixas mostradas abaixo. Determine e exiba quantos
vendedores receberam salários nas seguintes faixas de valores:
a. $200 - $299 - b. $300 - $399 - c. $400 - $499 - d. $500 - $599 - e. $600 - $699 - f. $700 - $799 - g. $800 - $899 - h. $900 - $999 - i. $1000 em diante
Desafio: Crie uma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados. """
funcionarios = {}
lista = []
cont = a = b = c = d = e = f = g = h = i = 0
resposta = 'S'
while resposta == 'S':
    nome = str(input('Nome do vendedor: ')).capitalize()
    print('- ' * 15)
    bruto = float(input('Valor de vendas brutas: '))
    print('- ' * 15)
    porcentagem = 9 * bruto / 100
    total = 200 + porcentagem
    print(f'O vendedor [{nome}] recebeu um total de {total} reais.')
    if total < 300:
        funcionarios['faixa'] = 'a'
        funcionarios['nome'] = nome
        funcionarios['salario'] = total
        a += 1
    elif 300 <= total < 400:
        funcionarios['faixa'] = 'b'
        funcionarios['nome'] = nome
        funcionarios['salario'] = total
        b += 1
    elif 400 <= total < 500:
        funcionarios['faixa'] = 'c'
        funcionarios['nome'] = nome
        funcionarios['salario'] = total
        c += 1
    elif 500 <= total < 600:
        funcionarios['faixa'] = 'd'
        funcionarios['nome'] = nome
        funcionarios['salario'] = total
        d += 1
    elif 600 <= total < 700:
        funcionarios['faixa'] = 'e'
        funcionarios['nome'] = nome
        funcionarios['salario'] = total
        e += 1
    elif 700 <= total < 800:
        funcionarios['faixa'] = 'f'
        funcionarios['nome'] = nome
        funcionarios['salario'] = total
        f += 1
    elif 800 <= total < 900:
        funcionarios['faixa'] = 'g'
        funcionarios['nome'] = nome
        funcionarios['salario'] = total
        g += 1
    elif 900 <= total < 1000:
        funcionarios['faixa'] = 'h'
        funcionarios['nome'] = nome
        funcionarios['salario'] = total
        h += 1
    else:
        funcionarios['faixa'] = 'i'
        funcionarios['nome'] = nome
        funcionarios['salario'] = total
        i += 1
    lista.append(funcionarios.copy())
    cont += 1
    resposta = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    while resposta not in 'SN':
        resposta = str(input('Erro! Digite novamente, quer continuar [S/N]: ')).strip().upper()[0]
    print('-*' * 15)

print(f'Na faixa A temos {a} pessoas.')
print(f'Na faixa B temos {b} pessoas.')
print(f'Na faixa C temos {c} pessoas.')
print(f'Na faixa D temos {d} pessoas.')
print(f'Na faixa E temos {e} pessoas.')
print(f'Na faixa F temos {f} pessoas.')
print(f'Na faixa G temos {g} pessoas.')
print(f'Na faixa H temos {h} pessoas.')
print(f'Na faixa I temos {i} pessoas.')

#Falta completar o desafio e melhorar a mostragem.