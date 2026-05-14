print('- - - Programa de PG - - -')
p = int(input('Digite o primeiro termo da PG: '))
q = int(input('Digite a razão da PG: '))
n = int(input('Digite a quantidade de termos da PG: '))
cont = 0
sn = p * ((q ** n) - 1) / (q - 1)
print(p)
while cont < n-1:
    p = p * q
    #print(p, end=' ')
    print(p)
    cont += 1
print(f'A soma de todos os {n} termos da PG é {sn}')

