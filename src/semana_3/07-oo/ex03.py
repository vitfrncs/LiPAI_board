"""crie uma classe Participacao que deve ter como atributos codigo, data inicio, data fim, aluno e o projeto associado."""

class Participacao:
    def __init__(self, codigo, data_inicio, data_fim, aluno, projeto_associado):
        self.codigo = codigo
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.aluno = aluno
        self.projeto_associado = projeto_associado

    def __eq__(self, outro):
        return isinstance(outro, Participacao) and self.codigo == outro.codigo

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        if not valor:
            raise ValueError(f"Código inválido: {valor}")
        self._codigo = valor

    @property
    def data_inicio(self):
        return self._data_inicio

    @data_inicio.setter
    def data_inicio(self, valor):
        if not valor:
            raise ValueError(f"Data de início inválida: {valor}")
        self._data_inicio = valor

    @property
    def data_fim(self):
        return self._data_fim

    @data_fim.setter
    def data_fim(self, valor):
        if not valor:
            raise ValueError(f"Data de fim inválida: {valor}")
        self._data_fim = valor

    @property
    def aluno(self):
        return self._aluno

    @aluno.setter
    def aluno(self, valor):
        if not valor:
            raise ValueError(f"Aluno inválido: {valor}")
        self._aluno = valor

    @property
    def projeto_associado(self):
        return self._projeto_associado

    @projeto_associado.setter
    def projeto_associado(self, valor):
        if not valor:
            raise ValueError(f"Projeto associado inválido: {valor}")
        self._projeto_associado = valor