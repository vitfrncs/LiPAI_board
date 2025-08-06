"""crie uma classe Aluno que deve ter como atributos o prontuario, nome e email. Deve ser possível construir um 
   objeto aluno a partir da string prontuario,nome,email ex: SP0101,João da Silva,joao@email.com . Nenhum dos atributos 
   pode ser vazio ou nulos (utilizar propriedades). Dois alunos podem ser considerados iguais caso tenham o mesmo prontuário."""

class Aluno:
    def __init__(self, prontuario, nome, email):
        self.prontuario = prontuario
        self.nome = nome
        self.email = email

    @classmethod
    def from_string(cls, dados):
        try:
            prontuario, nome, email = [v.strip() for v in dados.split(',')]
        except ValueError:
            raise ValueError("Formato inválido. Esperado: prontuario,nome,email")
        return cls(prontuario, nome, email)

    def __eq__(self, other):
        return isinstance(other, Aluno) and self.prontuario == other.prontuario

    @property
    def prontuario(self):
        return self._prontuario

    @prontuario.setter
    def prontuario(self, value):
        if not value:
            raise ValueError("Prontuário não pode ser vazio.")
        self._prontuario = value

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        if not value:
            raise ValueError("Nome não pode ser vazio.")
        self._nome = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not value:
            raise ValueError("Email não pode ser vazio.")
        self._email = value


# Exemplo de uso:
aluno1 = Aluno("0101", "João", "joao@eumail.com")
aluno2 = Aluno.from_string("SP0101, João, joao@eumail.com")
aluno3 = Aluno("0102", "Maria", "maria@email.com")

print(f"aluno1 == aluno2: {aluno1 == aluno2}")  
print(f"aluno1 == aluno3: {aluno1 == aluno3}") 
print(f"aluno2 details: {aluno2.prontuario}, {aluno2.nome}, {aluno2.email}")