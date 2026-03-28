n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
if n1 > n2:
    print('O PRIMEIRO valor é \033[4m\033[1mMAIOR\033[m.')
elif n2 > n1:
    print('O SEGUNDO valor é \033[4m\033[1mMAIOR\033[m.')
else:
    print('Os dois valores são \033[1m\033[4mIGUAIS\033[m.')
