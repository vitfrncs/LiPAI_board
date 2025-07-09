"""Implementar ex02 com dicionário"""

meses = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro"
}

numero_mes = int(input("Digite o número do mês (1 a 12): "))

if numero_mes in meses:
    mes = meses[numero_mes]
    print(f"O mês correspondente é: {mes}")
else:
    print("Número digitado é inválido.")
