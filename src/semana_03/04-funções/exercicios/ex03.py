"""crie uma função que recebe uma tupla de números como parâmetro (numeros) e retorna a soma dos números"""

def somar_numeros(numeros):
    soma = 0
    for numero in numeros:
        soma += numero
    return soma

tupla = (10.0, 3.0, 6.0)
resultado = somar_numeros(tupla)
print(f"A soma é: {resultado}")
