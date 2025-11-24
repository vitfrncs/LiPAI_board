"""AUla 01 - Manipulando arquivos"""

# open("caminho", "r")

#MODE
# r leitura
# a append / incrementar
# w escrita
# x criar arquivo
# r+ leitura + escrita

arquivo = open("src/06-arquivos/teste.txt", "a")

# print(arquivo.readable()) # arquivo pode ser lido ou não
# print(arquivo.read())
# print(arquivo.readline()) # lê linha por linha se for chamdo de novo
# lista = arquivo.readlines() # transforma conteudo do arquivo em uma lista

# print(lista)
# print(lista[3])

arquivo.write("\nSQL")
# Usar o write com o modo w apagaria todo o arquivo e substituiria com o conteúdo do write
# Dá para usar o w para criar arquivos, assim como x
arquivo2 = open("src/06-arquivos/teste2.txt", "w")
arquivo2 = open("src/06-arquivos/teste3.txt", "x")

import os 

if os.path.exists("src/06-arquivos/teste3.txt"):
    os.remove("src/06-arquivos/teste3.txt")
else:
    print("Arquivo não existe")

# os.rmdir('src/06-arquivos/pasta') # remove pasta (só remove se a pasta estiver vazia)

arquivo.close()
arquivo2.close()
