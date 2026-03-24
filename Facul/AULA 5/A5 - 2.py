n = 10
sp = 0
sn = 0
while n != 0:
    n = int(input('Digite o número: '))
    if n > 0:
        sp += n
    else:
        sn += n
print('Total dos positivos: {}'.format(sp))
print('Total dos negativos: {}'.format(sn))