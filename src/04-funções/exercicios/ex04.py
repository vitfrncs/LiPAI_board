"""crie uma função que recebe vários argumentos numéricos através do *args retorna a soma dos números"""
# é mais prático para chamadas diretas:

def somar_numeros(*args):
    soma = 0
    for numero in args:
        soma += numero
    return soma

resultado = somar_numeros(10.0, 3.0, 6.0)
print(f"A soma é: {resultado}")
