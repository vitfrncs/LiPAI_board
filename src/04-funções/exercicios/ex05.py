"""Utilizando as diretrizes de Índice de Massa Corporal (IMC) da Organização Mundial de Saúde (OMS),
crie uma calculadora em python que solicita ao usuário seu peso (Kg) e sua altura (m) e apresenta em
 qual classificação o indivíduo se encaixa. Além disso, o programa deve apresentar a situação atual do 
 indivíduo ('normal', 'perder peso', 'ganhar peso') com base na classificação Peso normal."""

def calcular_imc(individuo):
    peso = individuo["peso"]
    altura = individuo["altura"]
    imc = peso / (altura * altura)
    return imc


def obter_classificacao(imc):
    if imc < 18.5:
        return "Baixo peso"
    elif 18.5 <= imc <= 24.9:
        return "Peso normal"
    elif 25.0 <= imc <= 29.9:
        return "Excesso de peso"
    elif 30.0 <= imc <= 34.9:
        return "Obesidade de Classe 1"
    elif 35.0 <= imc <= 39.9:
        return "Obesidade de Classe 2"
    else:
        return "Obesidade de Classe 3"


def situacao_individuo(imc):
    if imc < 18.5:
        return "ganhar peso"
    elif 18.5 <= imc <= 24.9:
        return "normal"
    else:
        return "perder peso"

peso = float(input("Digite seu peso em Kg: "))
altura = float(input("Digite sua altura em metros: "))

individuo = {
    "peso": peso,
    "altura": altura
}

imc = calcular_imc(individuo)

classificacao = obter_classificacao(imc)

situacao = situacao_individuo(imc)

print(f"\nSeu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")
print(f"Situação: {situacao}")
