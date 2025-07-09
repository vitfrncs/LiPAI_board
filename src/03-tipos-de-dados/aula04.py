"""AUla 04 - Tipos de Dados - Dicionário"""

# dic (dicionário)
# coleção de key-value
# key: é única
# mutável

#criar um dicionário
carro = {
'marca': "ford",
'modelo': "Mustang",
'ano': 1964
}
print(carro, type(carro))

#acessar valores por chave
print(carro['marca'])
print(carro.get('marca'))

#pegar todas as chaves
print(carro.keys())
print(carro.values())
print(carro.items())

#verifica se a chave existe 
print('ano'in carro)
print('cor'in carro) # nao existe

#adicionando chave/valor de forma dinâmica
carro['cor'] = 'Azul'
print('cor'in carro) # existe!

#remover chave
marca = carro.pop('marca')
print(marca)
print(carro)

# loop
for key in carro:
    print(key, carro[key], type(key))

for value in carro.values():
    print(value)

for key in carro.keys():
    print(key)

for key, value in carro.items():
    print(key,value)

# lista de dicionarios 
aluno1 = {
    'nome': 'João',
    'email': 'joao@email.com',
    'notas': [10.0, 2.3, 10.0]
}

aluno2 = {
    'nome': 'Maria',
    'email': 'maria@email.com',
    'notas': [10.0, 7.3, 10.0]
}

alunos = [aluno1, aluno2]

# tomas cuidado com complexidade computacional
for aluno in alunos:
    print(aluno['nome', aluno['email']])
    for nota in aluno['notas']:
        print(nota)