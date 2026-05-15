""" O programa deve pedir que a pessoa digite seu nome. Em seguida, utilizando listas para armazenar as respostas, faça
5 perguntas para a pessoa sobre um crime. As perguntas são:
a. "Telefonou para a vítima?"
b. "Esteve no local do crime?"
c. "Mora perto da vítima?"
d. "Devia para a vítima?"
e. "Já trabalhou com a vítima?"
As respostas devem ser lidas como “SIM” e “NÃO” em letras maiúsculas. Qualquer outra coisa digitada não deve ser
aceita e a pergunta refeita.
No final o programa deve emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder
positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como
"Assassino". Caso contrário, ele será classificado como 'Inocente' """

lista = []
pessoa = {}
contagem = 0
pessoa['Nome'] = str(input('Nome: ')).capitalize()
print('- - - ' * 6)
pessoa['Telefonou para a vítima'] = str(input('Telefonou para a vítima: ')).strip().upper()[0]
while pessoa['Telefonou para a vítima'] not in 'SN':
    print('- - - ' * 6)
    pessoa['Telefonou para a vítima'] = str(input('ERRO, digite apenas Sim ou Não.\nTelefonou para a vítima: ')).strip().upper()[0]
print('- - - ' * 6)
pessoa['Esteve no local do crime'] = str(input('Esteve no local do crime: ')).strip().upper()[0]
while pessoa['Esteve no local do crime'] not in 'SN':
    print('- - - ' * 6)
    pessoa['Esteve no local do crime'] = str(input('Erro, digite apenas Sim ou Não.\nEsteve no local do crime: ')).strip().upper()[0]
print('- - - ' * 6)
pessoa['Mora perto da vítima'] = str(input('Mora perto da vítima: ')).strip().upper()[0]
while pessoa['Mora perto da vítima'] not in 'SN':
    print('- - - ' * 6)
    pessoa['Mora perto da vítima'] = str(input('Erro, digite apenas Sim ou Não.\nMora perto da vítima: ')).strip().upper()[0]
print('- - - ' * 6)
pessoa['Devia para a vítima'] = str(input('Devia para a vítima: ')).strip().upper()[0]
while pessoa['Devia para a vítima'] not in 'SN':
    print('- - - ' * 6)
    pessoa['Devia para a vítima'] = str(input('Erro, digite apenas Sim ou Não.\nDevia para a vítima: ')).strip().upper()[0]
print('- - - ' * 6)
pessoa['Já trabalhou com a vítima'] = str(input('Já trabalhou com a vítima: ')).strip().upper()[0]
while pessoa['Já trabalhou com a vítima'] not in 'SN':
    print('- - - ' * 6)
    pessoa['Já trabalhou com a vítima'] = str(input('Erro, digite apenas Sim ou Não.\nJá trabalhou com a vítima: ')).strip().upper()[0]
lista.append(pessoa.copy())
# Fazendo a contagem
if lista[0]['Telefonou para a vítima'] == 'S':
    contagem += 1
if lista[0]['Esteve no local do crime'] == 'S':
    contagem += 1
if lista[0]['Mora perto da vítima'] == 'S':
    contagem += 1
if lista[0]['Devia para a vítima'] == 'S':
    contagem += 1
if lista[0]['Já trabalhou com a vítima'] == 'S':
    contagem += 1
# Classificando
print('-*-' * 21)
if contagem == 2:
    print(f'{lista[0]['Nome']} é [SUSPEITO], porque respondeu SIM para [{contagem}] perguntas.')
elif contagem == 3 or 4:
    print(f'{lista[0]['Nome']} é [CÚMPLICE], porque respondeu SIM para [{contagem}] perguntas.')
elif contagem == 5:
    print(f'{lista[0]['Nome']} é [ASSASSINO], porque respondeu SIM para [{contagem}] perguntas.')
else:
    print(f'{lista[0]['Nome']} é INOCENTE.')
print('-*-' * 21)
