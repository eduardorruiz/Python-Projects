""" Modularização """
#Ajudam a organizar o código, facilita manutenção, ocultação do código detalhado e reutilização em outros projetos.

# É só criar uma função em um arquivo .py e no seu arquivo principal, você importa o seu arquivo .py
# Exemplos: no arquivo uteis.py tem a função fatorial e eu gostaria de usa-la, eu apenas preciso importa-la.
from uteis import fatorial # Importou apenas a função fatorial.
import uteis # Importou todas as funções que tenham em uteis.

""" Pacotes """
# Além da criação de módulos o python permite a criação de pacotes, que são diversos módulos separados.
# Os pacotes são as pastas e os módulos as subopastas, a fim de exemplificar:
# Você cria o PACOTE chamado "Módulos", dentro desse pacote tem os subpacotes "uteis", onde tem a função fatorial.
# OBS: todo pacote e subpacote(módulo), precisam ter o arquivo chamado "__init__.py", e nele  você coloca as coisas.

# COMO CRIAR: vc vai em new e seleciona o "python package" e esse vai ser o seu pacote principal, ai dentro desse pacote
# você cria a mesma coisa, para serem seus subpacotes.
