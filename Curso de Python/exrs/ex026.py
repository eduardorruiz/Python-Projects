frase = str(input('Digite a frase que será analisada: ')).strip().upper()
print(f'A letra A aparece {frase.count('A')} vezes.')
print(f'A letra A apareceu pela primeira vez na posição {frase.find('A') + 1}.')
print(f'A última letra A apareceu na posição {frase.rfind('A') + 1}.')