""" AUla 06 - Conversão de Tipos"""

# Conversão de tipo implicita e explicita:

leitura = 5.53
peso = 3
total = leitura * peso # conversão implicta de peso para float
print(total, type(total))

# python sempre tenta evitar a perda de dados (nesse caso, por meio da conversão implicita)

# Conversão explícita (type casting)
# soma = 13.4 + '3.5' # type error operador de soma não suporta floar e str
soma = 13.4 + float('3.5') 
print(soma, type(soma))

# soma = 13.4 + float('abc') #value error

idade = int('32')
print(idade, type(idade))

nome = 'Maria'
altura = 1.70


#mensagem = nome + ' tem a altura de ' + str(altura)
mensagem = f'{nome} tem a altura de {altura}'
print(mensagem) 