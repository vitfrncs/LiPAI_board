"""Aula 01 - Debug"""

def somar(n1,n2, n3):
    soma = n1 + n2 + n3
    return soma

def calcular_media(n1,n2,n3):
    soma = somar(n1,n2,n3)
    media = soma / 3
    return media


# breakpoint() # para o código na linha 14
nota1 = 10.0
nota2 = 3.0
nota3 = 5.5


# breakpoint() # para o código na linha 20
media = calcular_media(nota1, nota2, nota3)
print(media)