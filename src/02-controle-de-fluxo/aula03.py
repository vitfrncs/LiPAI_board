""" Aula 03 - loop for"""

# 1.iteração em coleção de elementos
# 2. Repetir instrução

linguagens = ['C', 'Python', 'Java']

print(linguagens[0])
print(linguagens[1])
print(linguagens[2])

# for valor in colecao:
#   instrucao
#   instrucao
#   instrucao

# Comportamento do operador in é diferente dependendo do contexto
print('Java' in linguagens) # booleano

for linguagem in linguagens:
    print(linguagem.upper())

nota1 = 10.0
nota2 = 5.5
nota3 = 8.3

media = (nota1 + nota2 + nota3) / 3
print(media)

notas = [10.0, 5.5, 8.3]

soma = 0.0
for nota in notas:
    soma = soma + nota

media = soma /len(notas)
print (media)

#range
# valores = range(10)
# valores = range(0,10)
# valores = range(0,10, 2)
valores = range(10,0, -1)

print(valores)

for valor in valores:
    print(valor)

for i in range(len(linguagens)):
    print(linguagens[i])