"""Crie um programa em python que recebe como entrada o comprimento, altura e a largura (cm) de um aquário 
e calcule as seguintes informações: O volume do aquário em litros; A potência do termostato necessária para 
manter a temperatura adequada dentro do aquário; A quantidade em litros de filtragem por hora necessária para 
manter a qualidade da água."""

def calcular_volume(aquario):
    c = aquario["comprimento"]
    a = aquario["altura"]
    l = aquario["largura"]
    volume = (c * a * l) / 1000
    return volume


def calcular_potencia_termometro(volume, temperatura_desejada, temperatura_ambiente):
    return volume * 0.05 * (temperatura_desejada - temperatura_ambiente)


def calcular_filtragem(volume):
    return volume * 2, volume * 3

# Entrada de dados 
comprimento = float(input("Comprimento do aquário (cm): "))
altura = float(input("Altura do aquário (cm): "))
largura = float(input("Largura do aquário (cm): "))

temperatura_ambiente = float(input("Temperatura ambiente (°C): "))
temperatura_desejada = float(input("Temperatura desejada (°C): "))

# dicionário com os dados
aquario = {
    "comprimento": comprimento,
    "altura": altura,
    "largura": largura
}


volume = calcular_volume(aquario)
potencia = calcular_potencia_termometro(volume, temperatura_desejada, temperatura_ambiente)
filtro_min, filtro_max = calcular_filtragem(volume)

print(f"\nVolume do aquário: {volume:.2f} litros")
print(f"Potência recomendada do termostato: {potencia:.2f} watts")
print(f"Filtragem recomendada: entre {filtro_min:.2f} L/h e {filtro_max:.2f} L/h")
