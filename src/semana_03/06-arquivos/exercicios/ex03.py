"""ex03.py com base nos códigos dos exercícios anteriores, crie a função linha_para_dict que recebe uma linha do arquivo (string), 
exemplo SP000001,Maria da Silva,maria@email.com , uma lista com os nomes das chaves do dicionário ['prontuario', 'nome', 'email'] 
e retorna o dicionário correspondente à aquele registro. Não utilizar bibliotecas ou funções prontas para leitura do arquivo. """

def converter_linha_em_dicionario(texto, chaves):
    valores = [valor.strip() for valor in texto.split(",")]

    if len(valores) != len(chaves):
        return None

    resultado = {}
    for indice, chave in enumerate(chaves):
        resultado[chave] = valores[indice]

    return resultado
