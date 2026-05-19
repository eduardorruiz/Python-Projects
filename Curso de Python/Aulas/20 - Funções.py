# as Funções são ROTINAS --> ex: print, input, int, float...

# Criando uma função para isso:
print('-----------')
print('APRENDENDO FUNÇÕES')
print('-----------')
#criando...
def mostralinha():
    print('-------------')
mostralinha()
print('Aprendendo funções')
mostralinha()

# Usando PARAMÊTROS:
def mensagem(msg):
    print('--' * 10)
    print(msg)
    print('--' * 10)

mensagem('EDUARDO') # Esse Eduardo é o parametro e vai ser substituído pelo msg

# Exemplos Práticos

a = 1
b = 10
s = a + b
print(s)
a = 2
b = 20
s = a + b
print(s)

#função
def soma(a, b):
    s = a + b
    print(s)
# programa principal
soma(1, 10)
soma(a=2, b=20)
soma(b=3, a=30) # pode inverter tranquilamente, mas precisa especificar tudo
# soma(1, 2, 3) vai dar erro pq só defini duas.

# Empacotar parâmetros
def contador(*num): # Isso gera uma TUPLA
    tam = len(num)
    print(f'Recebi os numeros {num} e são ao todo {tam} numeros.')
contador(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
contador(1, 2, 3, 4, 5)
contador(1)

# pra criar uma LISTA

def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1
# Programa principal
valores = [1, 2, 3, 4, 5]
print(valores)
dobra(valores)
print(valores)

# Desempacotamento
def soma(* valoress):
    s = 0
    for num in valoress:
        s += num
    print(f'Somando os valores {valores} temos {s}')

soma(10, 90)
soma(30, 30 , 30, 10)