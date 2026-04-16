"""Refaça o exercício anterior generalizando-o para N valores inteiros digitados no teclado, onde N é um número
fornecido pelo usuário. Esse N deve ser usado no programa ao invés do tamanho fixo de 10 sugerido no programa
anterior."""

LMin = int(input("Insira o valor do LMin: "))
LMax = int(input("Insira o valor do LMax: "))
N = int(input("Insira o valor do N: "))
A = []
cont = quantidadeefetiva = 0
if LMin < LMax:
    while cont < N:
        valor = int(input(f"Insira o {cont + 1}° elemento de A: "))
        cont += 1
        if valor <= LMax and valor >= LMin:
            A.append(valor)
            quantidadeefetiva += 1
        else:
            print("Valor invalido")
if LMin == LMax:
    print('Erro nos valores de LMin e LMax.')
if LMin > LMax:
    print('LMax é menor que LMin, portanto será usado o inverso.')
    while cont < N:
        valor = int(input(f"Insira o {cont + 1}° elemento de A: "))
        cont += 1
        if valor <= LMin and valor >= LMax:
            A.append(valor)
            quantidadeefetiva += 1
        else:
            print("Valor invalido")
print(f'A lista A é {A} e nela foram inseridos {quantidadeefetiva} elementos.')