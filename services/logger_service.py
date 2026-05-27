import json
from datetime import datetime
from pathlib import Path

class LoggerService:

    ARQUIVO = Path("logs/sistema.json")

    @classmethod
    def criar_arquivo_log(cls):

        if not cls.ARQUIVO.exists():
            cls.ARQUIVO.parent.mkdir(exist_ok=True)

            with open(cls.ARQUIVO,"w") as arquivo:

                json.dump({}, arquivo, ensure_ascii=False, indent=4)



    @classmethod
    def log(cls, usuario=None, acao=None, detalhe=None):
        cls.criar_arquivo_log()

        data_e_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        with open(cls.ARQUIVO, "a") as arquivo:
            arquivo.write(f"{data_e_hora}\n{usuario}\n{acao}\n{detalhe}\n")

