somaidade = 0
mulheresvinte = 0
maioridadehomem = 0
nomehomemvelho = ''
for p in range(1,5):
    print(f'----- {p}° PESSOA -----')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    somaidade += idade
    if idade <= 20 and sexo == 'F' or sexo == 'f':
        mulheresvinte += 1
    if p == 1 and sexo == 'M' or sexo == 'm':
        maioridadehomem = idade
        nomehomemvelho = nome
    if sexo == 'M' or sexo == 'm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomehomemvelho = nome
media = somaidade / 4
print(f'A média de idade do grupo é de {media} anos.')
print(f'Tem {mulheresvinte} mulheres com menos de 20 anos.')
print(f'O nome do homem mais velho é {nomehomemvelho} e tem {maioridadehomem} anos.')

