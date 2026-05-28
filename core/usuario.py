from core.tarefa import Tarefa


class Usuario():
    def __init__(self, id, nome, email, senha_hash):
        self.__id = id
        self.nome = nome
        self.__email = email
        self.__senha_hash = senha_hash
        self.tarefas = []



    def to_dict(self):

        dados = {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'senha_hash': self.senha_hash,
            'tarefas': [tarefa.to_dict() for tarefa in self.tarefas]
        }

        return dados


    @classmethod
    def from_dict(cls, dados):
        usuario = Usuario(
            dados['id'],
            dados['nome'],
            dados['email'],
            dados['senha_hash'],
        )

        usuario.tarefas = [Tarefa.from_dict(tarefa) for tarefa in dados['tarefas']]

        return usuario

    @property
    def email(self):
        return self.__email

    @property
    def id(self):
        return self.__id

    @property
    def senha_hash(self):
        return self.__senha_hash


    def adicionar_tarefa(self, tarefa):

        self.tarefas.append(tarefa)


    def remover_tarefa(self, id):

        tarefa = self.buscar_tarefa(id)

        if tarefa:

            self.tarefas.remove(tarefa)


    def buscar_tarefa(self, id):

        for tarefa in self.tarefas:

            if tarefa.id == id:

                return tarefa

        return None

