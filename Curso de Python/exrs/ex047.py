print('Contagem de números pares entre 1 - 50')
for cont in range(2, 51, 2):
    print(cont, end=' - ')

# OUTRO MODO SERIA colocar
# for cont in range(1, 51, 2):
#   if cont % 2 == 0:
#       print(cont)

# PRA TIRAR O ULTIMO TRAÇO
for n in range(2, 50, 2):
    print(n, end=' - ')
print('50.')
