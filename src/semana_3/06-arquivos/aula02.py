"""AULA 02 - Manipulando arquivos com python"""

arq = open('arquivo.txt', 'r+')

# lista = ['Olá\n', 'Caio\n']

# arq.write("Olá, Caio\n")
# arq.writelines(lista)
# modo write apaga tudo que tiver no arquivo

lista = ['Oi\n', 'Carol\n']
arq.writelines(lista)

l = arq.readlines()
print(l)

arq.close()

with open('arquivo.txt', 'r') as arq:
    for i in arq:
        print(i)

with open('arquivo.txt', 'rb') as arq:
    x = arq.read()
    print(type(x.decode()))

