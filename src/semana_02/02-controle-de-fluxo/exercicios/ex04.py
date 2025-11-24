""" implemente o ex03.py mas ao final do programa deve ser apresentado ao 
    usuário todos os problemas que o identificador informado possui (implementar 
    como list de erros): """

identificador = input('Digite o identificador de fucnionarios: ')
erros = []

if len(identificador) != 7:
    erros.append('O identificador não possui 7 caracteres')


if len(identificador) < 2 or identificador[0] != 'B' or identificador[1] != 'R':
    erros.append('O identificador não inicia com "BR"')


if len(identificador) < 7 or identificador[6] != 'X':
    erros.append('O identificador não finaliza com "X"')


if len(identificador) >= 6:
    parte_numerica = identificador[2:6]
    try:
        numero = int(parte_numerica)
        if not (1 <= numero <= 9999):
            erros.append('O número está fora do intervalo de 0001 a 9999')
    except ValueError:
        erros.append('A parte numérica não é composta por um número válido')
else:
    erros.append('A parte numérica não pôde ser verificada ')

if not erros:
    print('Identificador válido')
else:
    print('Erros encontrados:')
    for erro in erros:
        print('* ', erro)
