"""Refaça o exercício anterior de modo que os valores inválidos, ou seja, os que estão fora do intervalo [Min, Max]
sejam inseridos em uma segunda lista chamada R. Apresentar na tela a lista de valores aceitos (lista A) e a lista de
valores rejeitados (lista R), bem como o tamanho de cada um."""

LMin = int(input("Insira o valor do LMin: "))
LMax = int(input("Insira o valor do LMax: "))
N = int(input("Insira o valor do N: "))
A = []
R = []
cont = quantidadeefetiva = quantidaderejeitados = 0
if LMin < LMax:
    while cont < N:
        valor = int(input(f"Insira o {cont + 1}° elemento de A: "))
        cont += 1
        if valor <= LMax and valor >= LMin:
            A.append(valor)
            quantidadeefetiva += 1
        else:
            print("Valor invalido, logo vai para a lista de rejeitados.")
            R.append(valor)
            quantidaderejeitados += 1
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
            print("Valor invalido, logo vai para a lista de rejeitados.")
            R.append(valor)
            quantidaderejeitados += 1
print(f'A lista A é {A} e nela foram inseridos {quantidadeefetiva} elementos.')
print(f'Agora, a lista de valores inválidos é {R} e nela foram inseridos {quantidaderejeitados} elementos.')