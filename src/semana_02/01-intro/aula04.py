""" Aula 04 - Variáveis,Constantes e Literais"""

# Variável: container para guardar dados

numero = 10
print(numero)
print(type(numero))

# Em outras linguagens:
# int numero = 10
# No python, não é necessário pois há inferência de tipo
# Tipagem dinâmica: tipo é definido em tempo de execução de não de compilação

# multiplas atribuições:
nome, idade, endereco = 'Maria', 20, 'Rua das ...'
print(nome, idade, endereco)
# Não é uma boa prática usar multiplas atribuições


# atribui mesmo valor para várias variáveis
nome1 = nome2 = nome3 = 'João'
print(nome1, nome2, nome3)
# Não é um ponteiro
nome2 = 'Pedro'
print(nome1, nome2, nome3)


# snake_case:

# padrão para nomes da variáveis
id_funcionario = 209
salarioa_atual = 5000.50

# apara constantes:
# Upper case - snake_case

MAIORIDADE_CIVIL = 21
MAIORIDADE_PENAL = 18

print(MAIORIDADE_CIVIL, MAIORIDADE_PENAL)

# Literais:
# valores fixos no código
idade = 27
print(idade)
print(27)

# Numericos 
print(10, type(10))
print(10.5, type(10.5))

# String:
print('Maria', type('Maria'))
print("Maria", type("Maria"))
print("John's house")

# Booleano:
print(True, type(True))
print(False, type(False))

# None 
print(None, type(None))

# Coleções

# Lista (list)
# mutável
numeros = [1, 2, 3]
print(numeros,type(numeros))

# Tuple (tuple)
# é imutável
emails = ('joao@email.com', 'maria@email.com')
print(emails, type(emails))

# Conjunto (set)
# mesmo funcionamento de conjuntos matematicos
nomes = {'maria', 'joao', 'maria', 'pedro'}
print(nomes, type(nomes))

# Dicionário (dictionary)
aluno = {
    'prontuario': 123435,
    'nome': 'Maria da Silva',
    'idade': 34
}
print(aluno, type(aluno))