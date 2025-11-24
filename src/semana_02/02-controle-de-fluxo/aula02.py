"""Aula 02 - INSTRUÇÃO ifAula 02 - INSTRUÇÃO if"""

# if condicao:
#   instrucao
#   instrucao
#   instrucao
# elif condicao:
#   instrucao
#   instrucao
#   instrucao
# else:
#   instrucao  
#   instrucao
#   instrucao

codigo_cliente = 32
valor_desconto = 30.0
DESCONTO_ESPECIAL = valor_desconto >= 20.0

if DESCONTO_ESPECIAL:
    print('Desconto Especial :)')
    print(codigo_cliente)
else: 
    print('Sem desconto especial :(')

# nome tem que ter pelo menos 3 caracteres
nome = 'lo'

NOME_INVALIDO = len(nome) < 3

if NOME_INVALIDO:
    print('Nome deve ter pelo menos tres caracteres')
else:
    print('Nome válido')

# ou;

if not NOME_INVALIDO:
    print('Nome válido')
else:
    print('Nome deve ter pelo menos tres caracteres')

# nome tem que ter tres caracteres
# idade tem que ser maior ou igual a 18
# exibir todos os erros no final apenas

nome = 'lo'
idade = 17
erros =[]

NOME_INVALIDO = len(nome) < 3 
if NOME_INVALIDO:
    erros.append('Nome deve ter pelo menos 3 caracteres')

IDADE_INVALIDA = idade < 18
if IDADE_INVALIDA: 
    erros.append('Idade deve ser maior ou igual a 18')

# False: False, None, 0, 0.0, string vazia '', lista, tuple, set vazio 
# True: todo o resto 
if erros:
    print(erros)
else:
    print('Dados válidos :D')

# if elif else
#VERIFICA se um número é positivo negativo ou zero
numero = 3

if numero > 0:
    print('Maior que zero')
elif numero == 0:
    print('Zero')
else: 
    print('Menor que zero')

# calcule a media e verifique se as duas notas são validas antes do calculo
n1 = 7.2
n2 = 4.0

# melhor não usar ifs aninhados 

NOTA1_VALIDA = 0 <= n1 <= 10
NOTA2_VALIDA = 0 <= n2 <= 10

if NOTA1_VALIDA and NOTA2_VALIDA:
    media = (n1 + n2) / 2
    if media >= 6:
        print('Aprovado')
    elif media >= 4:
        print('Recuperacao')
    else:
        print('Reprovado')
else:
    print('Notas inválidas')
