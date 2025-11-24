"""crie uma classe Projeto que deve ter como atributos o  codigo (número inteiro que representa o código do projeto), 
   titulo e responsável (nome do professor responsável pelo projeto). Deve ser possível construir um objeto projeto a 
   partir da string codigo, titulo,responsavel ex: 1,Laboratório de Desenvolvimento de Software,Pedro Gomes . Nenhum 
   dos atributos pode ser vazio ou nulos (utilizar propriedades). Dois projetos podem ser considerados iguais caso 
   tenham o mesmo codigo."""

class Projeto:
    def __init__(self, codigo, titulo, responsavel):
        self.codigo = codigo
        self.titulo = titulo
        self.responsavel = responsavel

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
