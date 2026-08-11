from Módulos.ex115.interface import *

def arquivoExiste(nome):
    try:
        arquivo = open(nome, 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        arquivo = open(nome, 'wt+') # w = write, t = text, + = cria se não tiver
        arquivo.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def lerArquivo(nome):
    try:
        arquivo = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        contador = 0
        for linha in arquivo:
            contador += 1
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{contador}.{dado[0]:<25} {dado[1]:>3} anos')
    finally:
        arquivo.close()

def cadastrar(arquivo, nome = 'desconhecido', idade = 0):
    try:
        arquivo = open(arquivo, 'at')
    except:
        print('Erro na abertura do arquivo!')
    else:
        try:
            arquivo.write(f'{nome}; {idade}\n')
        except:
            print('Erro na escrita dos dados!')
        else:
            print(f'Novo registro de {nome} adicionado!')

