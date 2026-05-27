from datetime import datetime
from ProjetoNivel4.core.enums import StatusTarefa, Prioridade


class Tarefa():
    def __init__(self, id, titulo, descricao, prioridade, prazo=None):
        self.__id = id
        self.titulo = titulo
        self.descricao = descricao
        self.status = StatusTarefa.PENDENTE
        self.prioridade = prioridade
        self.data_criacao = datetime.now()
        self.prazo = prazo


    def to_dict(self):
        dados = {
            'id': self.__id,
            'titulo': self.titulo,
            'descricao': self.descricao,
            'prioridade': self.prioridade.value,
            'status': self.status.value,
            'data_criacao': self.data_criacao.isoformat(),
            'prazo': self.prazo.isoformat()
            if self.prazo
            else None,
        }

        return dados

    @classmethod
    def from_dict(cls, dados):

        prazo = (datetime.fromisoformat(dados['prazo'])
                 if dados['prazo']
                 else None
                 )

        tarefa = cls(
            dados['id'],
            dados['titulo'],
            dados['descricao'],
            Prioridade(dados['prioridade']),
            prazo
        )

        tarefa.status = StatusTarefa(dados['status'])

        tarefa.data_criacao = datetime.fromisoformat(dados['data_criacao'])

        return tarefa


    @property
    def id(self):

        return self.__id

    def concluir(self):

        self.status = StatusTarefa.CONCLUIDA


    def editar(self, titulo=None, descricao=None, prioridade=None, prazo=None):

        if titulo is not None:

            self.titulo = titulo

        if descricao is not None:

            self.descricao = descricao

        if prioridade is not None:

            self.prioridade = prioridade

        if prazo is not None:

            self.prazo = prazo



