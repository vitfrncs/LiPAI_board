""" AUla 05 - Tipos e dados"""

# Númericos
# int, float

idade = 20
peso = 70.5

print(idade, type(idade))
print(peso, type(peso))


#String
nome = 'João'
sobrenome = 'dos Santos'
nome_completo = nome + ' ' + sobrenome
print(nome_completo)

produto = 'Coca-cola'
# Usando interpolação de variáveis:
print(f'O cliente {nome} {sobrenome} comprou o produto {produto}')

# O cliente nome_completo comprou o produto produto

print(nome[0], nome[-1])

print(nome.lower(), nome.upper())

print(1, 4 ,3 ,4 ,5, sep='XXX')

# Boolean
ligado = True
print(ligado, type(ligado))

resultado = 10 < 3
print(resultado, type(resultado))

# Listas 
frutas = ['banana', 'uva', 'morango']
print(frutas)
print(frutas[0])
print(frutas[1])
print(frutas[2])
#print(frutas[3]) # index error

frutas[0] = 'banana nanica'
frutas.append('abacaxi')
print(frutas)
print(len(frutas))

for frutas in frutas:
    print(frutas.upper())

# Tupla:
codigos =('SP01', 'SP02', 'SP03')
print(codigos[0])

# codigos[0]= 'SP05  # type error

# Conjuntos:
resultado_sorteio = {10, 4, 3, 55, 9}
print(resultado_sorteio)

resultado_sorteio.add(23)
print(resultado_sorteio)

#Dicionario
funcionario = {
    'codigo': 123,
    'nome': 'Maria da SIlva',
    'salario': 7000.00
}

print(funcionario)
print(funcionario['codigo'])
print(funcionario['nome'])
print(funcionario['salario'])

print(funcionario.keys())
print(funcionario.values())

funcionario['salario'] = 5000.0
print(funcionario['salario'])
