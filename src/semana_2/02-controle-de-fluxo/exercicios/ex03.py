""" código identificador de funcionários de uma empresa contém 7 caracteres, inicia com a sequência de caracteres BR, em seguida apresenta
    um número inteiro entre 0001 e 9999 e finaliza com o caractere X. Exemplos válidos: BR0001X BR1236X BR9999X; Exemplos inválidos: br0001X 
    BR126X BR99999X BR9999Y;  Crie um programa em python que solicita ao usuário um identificador e apresenta se o que foi informado é um valor
    válido ou inválido."""


identificador = input('Digite o identificador de fucnionarios: ')

TAMANHO_VALIDO = len(identificador) == 7
PREFIXO_VALIDO = identificador[0] == 'B' and identificador[1] == 'R'
SUFIXO_VALIDO = identificador[6] == 'X'

NUMERO_VALIDO = False
if TAMANHO_VALIDO:
    parte_numerica = identificador[2:6]
    DIGITOS = parte_numerica.isdigit()
    if DIGITOS:
        numero = int(parte_numerica)
        NUMERO_VALIDO = 1 <= numero <= 9999

# Resultado final
if TAMANHO_VALIDO and PREFIXO_VALIDO and SUFIXO_VALIDO and NUMERO_VALIDO:
    print('Identificador válido')
else:
    print('Identificador inválido')
