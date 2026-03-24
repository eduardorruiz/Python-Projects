
import math
# from math import sqrt, ceil, floor
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print(f' A raiz de {num} é igual a {raiz}')
# sqrt square root = raiz quadrada
# ceil arredonda pra cima
# floor arredonda pra baixo
# trunc elimina da virgula em diante
# pow potencia = a **
# factorial == fatorial
print(f'Arredondando pra cima, a raiz de {num} fica aproximadamente {math.ceil(raiz)} ')
print(f'Arredondando pra baixo, a raiz de {num} fica aproximadamente {math.floor(raiz)}')
print(math.trunc(raiz))

#ele fala sobre colocar emojis também
# import random
# random.choice(lista) = vai escolher algo da lista
# random.shufle(lista) = embaralha a lista