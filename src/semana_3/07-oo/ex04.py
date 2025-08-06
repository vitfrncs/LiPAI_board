""" crie o atributo do tipo list participacoesna classe Projeto e implemente o método add_participacao
que recebe como parâmetro um objeto Participação e adiciona na lista."""

class Projeto:
    def __init__(self, codigo, titulo, responsavel):
        self.codigo = codigo
        self.titulo = titulo
        self.responsavel = responsavel
        self.participacoes = []  # Lista de objetos Participacao

    @classmethod
    def from_string(cls, texto):
        partes = [parte.strip() for parte in texto.split(",")]

        if len(partes) != 3:
            raise ValueError("Formato inválido. Esperado: codigo,titulo,responsavel")

        try:
            codigo = int(partes[0])
        except ValueError:
            raise ValueError(f"Código deve ser um número inteiro. Recebido: {partes[0]}")

        return cls(codigo, partes[1], partes[2])

    def add_participacao(self, participacao):
        from types import SimpleNamespace  # evita erro se Participacao ainda não estiver definida
        if not hasattr(participacao, 'codigo'):
            raise TypeError("O objeto passado não é uma instância válida de Participacao.")
        self.participacoes.append(participacao)

    def __eq__(self, outro):
        return isinstance(outro, Projeto) and self.codigo == outro.codigo

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        if valor is None or not isinstance(valor, int):
            raise ValueError(f"Código inválido: {valor}")
        self._codigo = valor

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, valor):
        if not valor:
            raise ValueError("Título não pode ser vazio.")
        self._titulo = valor

    @property
    def responsavel(self):
        return self._responsavel

    @responsavel.setter
    def responsavel(self, valor):
        if not valor:
            raise ValueError("Responsável não pode ser vazio.")
        self._responsavel = valor
