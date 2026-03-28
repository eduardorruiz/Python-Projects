nome = str(input('Qual é seu nome completo? ')).strip()
print(f'Analisando o nome, {nome}...')
print(f'Seu nome todo em maiusculo é {nome.upper()}')
print(f'Seu nome todo em minusculo é {nome.lower()}')
ns = nome.split()
first = nome.split()[0]
lenfirst = len(first)
print(f'O primeiro nome, {first}, tem {lenfirst} letras.')
# No segundo {} para não precisar criar mais nada, pode se usar apenas {len(first)}
# ficaria por exemplo dividido = nome,split()
# o primeiro nome é {dividido[0]} e tem {len(dividido[0])}
print(f'E seu nome completo, {nome}, tem {len(nome)-nome.count(' ')} letras.')
