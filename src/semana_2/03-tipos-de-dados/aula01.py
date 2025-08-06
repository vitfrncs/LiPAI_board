""" AUla 01 - Tipos de Dados - Listas"""

#lista 
# ordenadas
# mutáveis
# indexáveis

nomes = ['Maria', 'Pedro', 'Joao']
print(nomes, type(nomes))

#formas de acessar elementos
print(nomes[0])
print(nomes[:2])
print(nomes[0:2])
print(nomes[1:])

# modificar elementos
nomes[0] = 'Maria da Silva'
nomes[1:] = ['Pedro da Silva', 'Joao Santos']
print(nomes)

#tamanho de uma lista 
#funcao len
print(len(nomes))

#adicionar elementos na lista
#metodo append
nomes.append('Marta Gomes')
print(nomes)

#metodo insert
nomes.insert(0, 'Guilherme Tavares')
print(nomes)

nomes.insert(2, 'Ana Clara')
print(nomes)

# metodo extend
nomes2 =['Kaio SIlva', 'Carlos Lopes']
print(len(nomes))
nomes.extend(nomes2)
print(nomes)
print(len(nomes))

#remover elemento
# metodoremove
nomes.remove('Maria da Silva')
print(nomes)
#del 
del nomes[0]
print(nomes)

# # remove lista da memoria
# del nomes
# print(nomes)

#limpar a lista
# método clear
nomes.clear()
print(nomes)

# iteração em lista 
for nome in nomes:
    print(nome)

print('----------')

for i in range(len(nomes)):
    print(nomes[i])