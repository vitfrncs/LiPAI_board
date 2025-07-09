"""Solicite ao usuário 3 notas e apresente o resultado da média aritmética das notas"""

notas = []
for i in range(0, 3):
    nota = float(input(f'Digite a nota {i}: '))
    notas.append(nota)

media = sum(notas) / len(notas)
print(f'Média: {media:.2f}')