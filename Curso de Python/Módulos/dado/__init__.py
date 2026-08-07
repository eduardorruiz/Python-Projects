def leiadinheiro(mensagem):
    válido = False
    while not válido:
        entrada = str(input(mensagem)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print('ERRO: "" é um preço inválido!')
        else:
            válido = True
            return float(entrada)

def leiaint(mensagem):
    n = input(mensagem).strip()
    while not n.isnumeric():
        print('ERRO, digite um número inteiro válido!')
        n = input(mensagem).strip()
    return int(n)