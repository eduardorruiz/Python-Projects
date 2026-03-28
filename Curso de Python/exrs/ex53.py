print('{:-^50}'.format(' ANALISADOR DE PALÍNDROMOS '))
frase = str(input('Digite a palavra que será verificada: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
# OU TIRA A LINHA 7,8 e 9 e coloca
#inverso = junto[::-1] por fatiamento
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print('Temos um PALÍNDROMO!')
else:
    print('a frase NÃO É UM PALÍNDROMO.')

