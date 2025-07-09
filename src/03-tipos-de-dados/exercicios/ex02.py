""" solicite ao usuário o mês do ano no formato numérico 1, 2, 3 ..12 e apresente o nome do ano. 
    Exemplo: entrada 3 saída ‘Março’.  IMplementar com tupla"""

# tupla com meses
meses = (
    "Janeiro", "Fevereiro", "Março", "Abril",
    "Maio", "Junho", "Julho", "Agosto",
    "Setembro", "Outubro", "Novembro", "Dezembro"
)

numero_mes = int(input("Digite o número do mês (1 a 12): "))

# Verificar se está no intervalo válido
if 1 <= numero_mes <= 12:
    mes = meses[numero_mes - 1]
    print(f"O mês digitado é: {mes}")
else:
    print("Número invalido")
