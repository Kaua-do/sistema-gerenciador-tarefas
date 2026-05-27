from datetime import datetime

from rich import print

class InputValidator:

    @classmethod
    def ler_int(cls, msg):
        while True:
            try:
                valor = int(input(msg))
            except TypeError:
                print('[red]ERRO! Digite um número inteiro válido!')
            else:
                return valor



    @classmethod
    def ler_str(cls, msg):
        while True:
            try:
                string = str(input(msg))
            except TypeError:
                print('[red]ERRO! Digite apenas letras!')
            else:
                return string


    @staticmethod
    def ler_data(msg):
        while True:

            data_str = input(msg).strip()

            if not data_str:
                return None

            try:

                return datetime.strptime(data_str, '%d/%m/%Y')

            except ValueError:

                print(
                    "[red]Data invlálida!"
                    "Use DD/MM/AAAA"
                )


    @staticmethod
    def impedir_vazio(msg):
        while True:

            frase = input(msg)

            if not frase:
                print('[red]ERRO! Este campo é obrigatório.')

            else:
                return frase


    @classmethod
    def confirmar(cls, msg):
        while True:

            resposta = input(msg).strip().lower()

            if resposta == "s":

                return True

            elif resposta == "n":

                return False

            print('[red]ERRO! Digite "S" ou "N"!')



