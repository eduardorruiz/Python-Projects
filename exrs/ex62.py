# MUITO DIFICIL
print('{:-^40}'.format(' 10 Termos de uma PA '))
pt = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
contador = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while contador <= total:
        resultado = pt + razao * (contador - 1)
        contador += 1
        print(resultado)
    print('-=-' * 25)
    mais = int(input('Quantos termos você quer mostrar a mais: '))
print('Fim do Programa')