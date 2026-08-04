""" INTERACTIVE HELP --> É a função help() ------------------------------------------------------------------------ """
# No console dar um help()
# Você pode digitar qualquer comando, função ou biblioteca, que vai te dar um manual.
# Pra sair é só digitar quit
# No programa é só usar como uma função normal e rodar o programa
# ex: help(print) --> e pronto vai aparecer o manual ao rodar o prog.

""" DOCSTRINGS --> é a documentação de uma função.----------------------------------------------------------------- """
# Para criar você precisa dar """escrever a documentação""".
# Logo após da linha da função.
# ex: def contador(i, f):
#     """ i = inicio, f = final """
# Agora é só dar um help(contador), que vai aparecer a documentação criada.

""" PARAMETROS OPICIONAIS -------------------------------------------------------------------------------------------- """
def somar(a, b, c):
    soma = a + b + c
    print(f'A soma vale {soma}.')
somar(2, 3, 5) # a=2, b=3 e c=5
somar(2, 3) # Como não tem o valor de C daria erro.
# Por isso entra os OPICIONAIS.
def somarcomopicionais(a, b, c = 0):
    soma = a + b + c
    print(f'A soma vale {soma}.')
# Agora o somar(2, 3) daria certo porque a gente def que caso não tenha o c --> c = 0.
somarcomopicionais(2, 3)
# Claro que podemos fazer isso com todos os parametros.

""" ESCOPO DE VARIAVEIS ---------------------------------------------------------------------------------------------- """
def teste(b):
    b += 1 # ESCOPO LOCAL, pq está dentro da função.
    c = 2 # ESCOPO LOCAL, pq está dentro da função.
    print(f' A dentro vale {a}') # --> 5 / Funciona certo pq o escopo é global.
    print(f' B dentro vale {b}') # --> 6 / Funciona pq o escopo é local e estamos no local.
    print(f' C dentro vale {c}') # --> 2 / Funciona pq o escopo é local e estamos no local.
a = 5 # ESCOPO GLOBAL
teste(a)
print(f' A fora vale {a}') # --> 5 / Funciona pq é escopo global.
print(f' B fora vale {b}') # Daria erro pq o escopo é local.
print(f' C fora vale {c}') # Daria erro pq o escopo é local.

# MAS, se eu criar uma variavel a dentro da função teste, o programa teria duas variaveis "a", uma sendo local da função teste e outra global.
# Segue o exemplo:
def teste2(b):
    a = 1000
    b += 1 # ESCOPO LOCAL, pq está dentro da função.
    c = 2 # ESCOPO LOCAL, pq está dentro da função.
    print(f' A dentro vale {a}') # --> 8(a local) / Funciona certo pq o escopo é global.
    print(f' B dentro vale {b}') # --> 9(faz a soma com o global) / Funciona pq o escopo é local e estamos no local.
    print(f' C dentro vale {c}') # --> 2 / Funciona pq o escopo é local e estamos no local.
a = 5 # ESCOPO GLOBAL
teste2(a)
print(f' A fora vale {a}') # --> 5 (a global) / Funciona pq é escopo global.
print(f' B fora vale {b}') # Daria erro pq o escopo é local.
print(f' C fora vale {c}') # Daria erro pq o escopo é local.

# Para tranformar uma variavel local para global:
def teste3(b):
    global a # Transformou o a = 1000, em global.
    a = 1000
    b += 1 # ESCOPO LOCAL, pq está dentro da função.
    print(f' A dentro vale {a}') # --> 8(a local) / Funciona certo pq o escopo é global.
    print(f' B dentro vale {b}') # --> 9(faz a soma com o global) / Funciona pq o escopo é local e estamos no local.
a = 5 # ESCOPO GLOBAL
teste3(a)
print(f' A fora vale {a}') # --> 1000 (a global) / Funciona pq é escopo global.
print(f' B fora vale {b}') # ERRO - pq o escopo é local.

""" RETORNO DE VALORES ----------------------------------------------------------------------------------------------"""
def somar2(a=0, b=0, c=0):
    soma = a + b + c
    print(f'A soma vale {soma}.')
somar2(2, 3, 5) # primeira soma = 10
somar2(2) # segunda soma = 2
# Depois que a primeira soma for feita, vamos perder o 10 e ficar apenas com o resultado da segunda soma.
# E isso é um problema, por isso usamos a função return
def somarcomretorno(a=0, b=0, c=0):
    soma = a + b + c
    return soma
resposta1 = somarcomretorno(2, 3, 5) # primeira soma = 10
resposta2 = somarcomretorno(2) # segunda soma = 2
print(f'As respostas foram: {resposta1} e {resposta2}.')

# OUTRO EXEMPLO:
def par(n = 0):
    if n % 2 == 0:
        return True
    else:
        return False
num = 5
print(par(num)) # Mostra FALSE.
num2 = 10
print(par(num2)) # Mostra TRUE.
