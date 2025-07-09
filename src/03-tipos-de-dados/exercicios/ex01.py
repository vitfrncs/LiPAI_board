"""Solicite ao usuário 3 números, armazene esses elementos em uma lista e apresente no final o menor e maior elemento"""

numeros = []

for i in range(3):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

menor = numeros[0]
maior = numeros[0]

for num in numeros:
    if num < menor:
        menor = num
    if num > maior:
        maior = num

print(f"O menor número é: {menor}")
print(f"O maior número é: {maior}")
