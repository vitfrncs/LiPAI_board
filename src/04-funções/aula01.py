"""Aula 01 - Introdução a funções"""

# Função é um bloco que realiza uma terafa especifica
# Divido um problema em pequenas partes
# Evitar repetição de código

#1. Standart LIbrary Functions - built-in functions
#ex: print, len

print('Olá', 123, True)

nomes =['Joao', 'Maria']
tamanho_lista = len(nomes)
print(nomes, tamanho_lista)

# 2. User Defined Functions:
# Definidas pelo desenvolvedor
# Fazerem parte da solução do problema

# declara
# nome: saudacoes
# parametros: nenhum
# retorno: nenhum
def saudacoes():
    print('Olá')

# chamada
saudacoes()
saudacoes()
saudacoes()


# declara
# nome: saudacoes
# parametros: nome
# retorno: nenhum
def saudacoes(nome):
    print(f'Olá {nome}')


#chamada
# valores, variáveis, expressões +> argumentos
#'Maria' é um argumento passado para o parametro nome
saudacoes('Maria')
saudacoes('João')
nome = 'CArlos'
saudacoes(nome)

#Declaração
# nome:calcular_media
# parametros: nota1, nota2, nota3
# retorno: nenhum
def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    print(media)

# Chamada
#argumentos sçao literais
calcular_media(10.0, 3.0, 6.0)
n1 = 10.0
n2 = 3.0
n3 = 8.0

#argumentos sâo variaveis

calcular_media(n1, n2, n3)

#Declaração
# nome:calcular_media
# parametros: nota1, nota2, nota3
# retorno: media
def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media

media = calcular_media(10.0, 3.0, 6.0)
print('media:', media)
