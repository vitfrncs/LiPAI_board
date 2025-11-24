"""- [ ]  `ex01.py` crie a função `carregar_dados_alunos` que recebe como parâmetro o nome de um arquivo que contém dados de
 alunos e retorna uma tupla, onde cada elemento é um dicionário com as seguintes chaves: prontuario, nome e email arquivo de dados"""

def carregar_dados_alunos(nome_arquivo):
    arquivo = open(nome_arquivo, "r")
    linhas = arquivo.readlines()
    arquivo.close()

    alunos = []

    for linha in linhas:
        linha = linha.strip()  # remove espaços e \n
        partes = linha.split(",")
        if len(partes) == 3:
            aluno = {
                'prontuario': partes[0].strip(),
                'nome': partes[1].strip(),
                'email': partes[2].strip()
            }
            alunos.append(aluno)

    return tuple(alunos)


dados = carregar_dados_alunos("alunos.txt")
for aluno in dados:
    print(aluno)


