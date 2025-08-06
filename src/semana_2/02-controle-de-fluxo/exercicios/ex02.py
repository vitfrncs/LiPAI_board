"""Solicite ao usuário uma única a vez as notas no formato n1, n2, n3, nm e apresente o resultado da média aritmética das 
   notas se está aprovado (maior que 6.0), recuperação (entre 4.0 e 6.0) ou reprovado (menor que 4.0)."""

entrada = input('Digite as notas (use espaço para separá-las): ')
notas = [float(n.strip()) for n in entrada.split()]

if notas: # se notas for vazio, a condição é falsa
    media = sum(notas) / len(notas)
    print(f'Média: {media:.2f}')
    
    if media > 6.0:
        print('Situação: Aprovado :D')
    elif media >= 4.0:
        print('Situação: Recuperação :|')
    else:
        print('Situação: Reprovado :(')
else:
    print('Nenhuma nota válida (num real) foi informada.')
