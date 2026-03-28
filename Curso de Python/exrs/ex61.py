print('{:-^40}'.format(' 10 Termos de uma PA '))
pt = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
contador = 1
while contador <= 10:
    resultado = pt + razao * (contador - 1)
    contador += 1
    print(resultado)
print('-=-' * 25)
