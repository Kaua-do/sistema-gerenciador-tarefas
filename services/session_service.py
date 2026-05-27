from datetime import datetime

from ProjetoNivel4.core import usuario
from ProjetoNivel4.services.logger_service import LoggerService

class SessionLogger:
    usuario = None
    inicio_sessao = None

    @classmethod
    def iniciar(cls, usuario):

        cls.usuario = usuario
        cls.inicio_sessao = datetime.now()

        LoggerService.log(
            f"LOGIN: {usuario.email}"
        )


    @classmethod
    def encerrar(cls):

        if not cls.usuario:
            return

        fim = datetime.now()

        duracao = fim - cls.inicio_sessao

        LoggerService.log(
            f"LOGOUT: {usuario.email}"
        )

        LoggerService.log(
            f"Duração da sessão: {duracao}"
        )

        cls.usuario = None
        cls.inicio_sessao = None