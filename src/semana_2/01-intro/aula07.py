"""Aula 07 = Entrada e SAída"""

#saída padrão - sys stdout
print('hello world', 'Maria', 1, True, sep='@', end='!!!\n')
# print('hello world', 'Maria', 1, True, sep='@', end='')

arquivo = open('nomes.txt', 'w', encoding='utf-8')

print('joao@email.com', 'maria@hotmail.com', 'pedor@yahoo.br', file=arquivo, sep=';')

#Entrada
# input
# nome = input('Digite seu nome: ')
# idade = int(input('Digite sua idade: '))

# print(type(nome), type(idade))

# if idade >= 18: 
#     print(f'{nome}, voce é maior de idade')
# else:
#     print(f'{nome}, voce é menor de idade')

# file
# arquivo como entrada de daos
arquivo_notas = open('notas.txt', 'r', encoding='utf-8')
conteudo = arquivo_notas.read()
notas = conteudo.split(sep=';')
notas = [float(nota) for nota in notas]
print(notas)

media = (notas[0] + notas[1] + notas[2]) / len(notas)
print(media)