# Exercícios de LISTA pt2 --> 84 a 89
""" Listas parte 2 """

dados = list()
dados.append("Eduardo")
dados.append(18)
dados.append('Henry')
dados.append(13)
dados.append('Kaleb')
dados.append(8)

pessoas = list()
pessoas.append(dados[:]) # Adicionei uma cópia dos dados em pessoas
# Dentro de pessoas o elemento zero é [Eduardo | 18]
# Mas dentro do elemento zero de pessoas --> Eduardo = elemento [0] e 18 = elemento [1]
pessoas = [['Eduardo', 18], ['Henry', 13], ['Kaleb', 8]] # Outro jeito de declarar listas compostas

print(pessoas[0][0]) # Mostra dentro do elemento [0] de pessoas, o elemento [0] = Eduardo
print(pessoas[1][1]) # Mostra dentro do elemento [1] de pessoas, o elemento [1] = 13
print(pessoas[2][0]) # Mostra dentro do elemento [2] de pessoas, o elemento [0] = Kaleb
print(pessoas[1]) # Mostra tudo = ['Henry', 13]

# VAI MOSTRAR --> Enzo tem 16 anos. --> Manuela tem 17 anos. --> ...
galera = [['Enzo', 16], ['Manuela', 17], ['Diniz', 15]]
for pessoa in galera:
    print(f'{pessoa[0]} tem {pessoa[1]} anos.')

# Vai ler o nome e a idade, com a lista dados e, adicionar na lista da turma
turma = list()
dadostemporarios = list()
for cont in range(0, 3):
    dadostemporarios.append(str(input('Nome: ')))
    dadostemporarios.append(int(input('Idade: ')))
    galera.append(dadostemporarios[:])
    dadostemporarios.clear() # Limpa os dados
print(turma)
# Mostrar as pessoas com 18 ou + anos
contagemmaior = contagemmenor = 0
for pessoa in turma:
    if pessoa[1] >= 18:
        print(f'{pessoa[0]} é maior de idade, tem {pessoa[1]} anos.')
        contagemmaior += 1
    else:
        print(f'{pessoa[0]} tem menos de 18 anos, tem {pessoa[1]} anos.')
        contagemmenor += 1
print(f'Temos {contagemmaior} pessoas com +18 e {contagemmenor} pessoas com menos de 18 anos.')