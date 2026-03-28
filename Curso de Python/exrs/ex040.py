n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
if media >= 7:
    print(f'Sua média foi {media}; \033[1;32mAPROVADO\033[m!!')
elif 7 > media >= 5:
    print(f'Sua média foi {media}; \033[1;33mRECUPERAÇÃO\033[m!!')
elif media < 5:
    print(f'Sua média foi {media}; \033[1;31mREPROVADO\033[m!!')
