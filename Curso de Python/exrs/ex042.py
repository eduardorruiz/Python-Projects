print('-=-' * 25)
print('Esse programa analisa e classifica os triângulos formados.')
print('-=-' * 25)
n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
n3 = float(input('Terceiro valor: '))
if n1 <= n2 + n3 and n2 <= n1 + n3 and n3 <= n1 + n2:
    print('Os valores acima \033[4mPODEM\033[m formar um triângulo!')
    print('E o triângulo formado será', end=' ')
    if n1 == n2 == n3:
        print('\033[1mEQUILÁTERO\033[m.')
    elif n1 != n2 != n3 != n1:
        print('\033[1mESCALENO\033[m.')
    else:
        print('\033[1mISÓCELES\033[m.')
else:
    print('Os valores acima \033[4mNÃO PODEM\033[m formar um triângulo!')
