# Exercicios de IF e ELIF --> 36 a 45
# Quando se tem uma condição com + de 2 caminhos: usa-se elif(else+if)
nome = str(input('Qual é seu nome? '))
if nome == 'Eduardo' or nome == 'Deivson' or nome == 'Thais':
    print(f'Que belo nome juvenil, {nome}.')
elif nome == 'Carlos' or nome == 'Norma':
    print(f'Que nome de coroa ein, {nome}.')
elif nome == 'Henry' or nome == 'Kaleb':
    print(f'Que nome infantil, {nome}.')
elif nome in 'Daniela Walter':
    print('Vocês são sogros do Eduardo correto?')
elif nome == 'Pietra':
    print(f'Seu nome em breve será {nome} Paesani Ruiz!!!')
else:
    print(f'{nome}, você não faz parte da Família Rocha Ruiz Araujo ne?')
print(f'Bom te ver nesse programa, volte sempre {nome}.')