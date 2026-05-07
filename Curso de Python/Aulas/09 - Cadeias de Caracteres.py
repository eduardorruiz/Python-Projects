# Exercícios de manipulação de texto --> 22 a 27
frase = 'Saudades da Pietra'
# FATIAMENTO
print(frase[12])
print(frase[12:18])
print(frase[12:18:2])
print(frase[:8])
print(frase[9:])
print(frase[12::3])
# ANALISE
len(frase) # para ver o tamanho da frase
frase.count('a') #conta quantos a tem em frase
frase.count('a',0,13) #conta quantos a tem de 0 até o 12
frase.find('Pie') #encontra, e indica o número onde está o P (posição)
frase.find('Eduardo') # EDUARDO não existe então vai mostrar -1
'Pietra'in frase #se tiver vai aparecer True
# TRANSFORMAÇÃO
frase.replace('Pietra','Neymar') # troca...
frase.upper() # deixa maiusculo
frase.lower() # deixa minusculo
frase.capitalize() # joga tudo pra minusculo e o primeiro item da str ficará maiusculo
frase.title() # faz o capitalize em todas as palavras, ent toda palavra ficará apenas com a primeira letra maiuscula
frase.strip() # remove os espaços inuteis(do cmc e do fim)
frase.rstrip() # remove espaços só de right(direita)
frase.lstrip() # remove espaços só de left(esquerda)
# DIVISÃO
frase.split() # onde tiver espaço vai dividir, cada nova palavra ficará com novas listas
# JUNÇÃO
'-'.join(frase) # vai juntar e colocar(-) onde ficavam os espaços p/ ter espaço = ' '
# 3 aspas
# print('''Ola dedadalfshfadsldalfhkahlsjlfajlj
#ajfghallkadskad~dajfçfaçafklçasflçajfalçsaçfka
#alfkçajflajfajkslfjalkfhjalfjalçjflajsflajlfjf''') # vai tudo, tlvz so com (""" a """)
