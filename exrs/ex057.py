sexo = str(input("Digite seu sexo [M/F]: ")).upper()
# while sexo not in ["M", "F"]:
while sexo != "M" and sexo != "F":
    print('Desculpe, não entendi.')
    if sexo != "M" and sexo != "F":
        sexo = str(input("Digite seu sexo novamente [M/F]: ")).upper()
if sexo == "M":
    print('Sexo válido, você é um homem.')
else:
    print('Sexo válido, você é uma mulher.')
