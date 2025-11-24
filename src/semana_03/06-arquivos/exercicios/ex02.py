"""ex02.py crie a função carregar_dados_projetos que recebe como parâmetro o nome de um arquivo que contém dados de projetos 
e retorna uma tupla, onde cada elemento é um dicionário com as seguintes chaves: codigo (número inteiro que representa o código 
do projeto), titulo e responsável (nome do professor responsável pelo projeto). Não utilizar bibliotecas ou funções prontas para 
leitura do arquivo."""

def carregar_dados_projetos(nome_arquivo):
    arquivo = open(nome_arquivo, "r")
    linhas = arquivo.readlines()
    arquivo.close()

    projetos = []

    for linha in linhas:
        linha = linha.strip() 
        partes = linha.split(",")
        
        if len(partes) == 3:
            codigo_str, titulo, responsavel = partes
            projeto = {
                'codigo': int(codigo_str.strip()),
                'titulo': titulo.strip(),
                'responsavel': responsavel.strip()
            }
            projetos.append(projeto)

    return tuple(projetos)

dados = carregar_dados_projetos("projetos.txt")

for projeto in dados:
    print(projeto)
