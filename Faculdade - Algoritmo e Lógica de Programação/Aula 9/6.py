"""Leia dois números inteiros LMin e LMax. Em seguida leia 10 valores inteiros e inserindo-os em uma lista A somente
se o valor fornecido estiver no intervalo [LMin, LMax]. Valores fora deste intervalo devem ser ignorados. Ao final,
apresentar a lista A e seu tamanho efetivo. Observe que para este programa funcionar apropriadamente é
necessário que LMin seja menor que LMax. Caso o usuário digite LMax menor que LMin, o programa deve inverter
os valores."""

LMin = int(input("Insira o valor do LMin: "))
LMax = int(input("Insira o valor do LMax: "))
A = []
cont = quantidadeefetiva = 0
if LMin < LMax:
    while cont < 10:
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
    while cont < 10:
        valor = int(input(f"Insira o {cont + 1}° elemento de A: "))
        cont += 1
        if valor <= LMin and valor >= LMax:
            A.append(valor)
            quantidadeefetiva += 1
        else:
            print("Valor invalido")
print(f'A lista A é {A} e nela foram inseridos {quantidadeefetiva} elementos.')