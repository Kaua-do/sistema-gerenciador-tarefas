from rich import print
from validators.input_validator import InputValidator
from services.auth_service import AuthService
from menus.task_menu import TaskMenu
from services.session_service import SessionLogger

class AuthMenu:
    def mostrar_menu(self):

        while True:

            print('[blue]1 - Login')
            print('[blue]2 - Cadastrar')
            print('[blue]3 - Sair')

            opcao = InputValidator.ler_int('Escolha uma opcao: ')

            match opcao:

                case 1:
                    try:
                        email = InputValidator.impedir_vazio('Informe o seu E-mail: ').strip()

                        senha = InputValidator.impedir_vazio('Informe a sua senha: ')

                        usuario = AuthService.login(email, senha)

                        print(f'[green]Bem-vindo(a) {usuario.nome}!')

                        SessionLogger.iniciar(usuario)

                        TaskMenu(usuario).mostrar_menu()

                        SessionLogger.encerrar()

                    except ValueError as erro:
                        print(f'[red]{erro}')

                case 2:
                    while True:
                        nome = InputValidator.ler_str('Informe o seu nome: ').strip()

                        try:
                            AuthService.validar_nome(nome)
                            break

                        except ValueError as erro:
                            print(f'[red]{erro}')

                    while True:
                        email = InputValidator.impedir_vazio('Informe o seu e-mail: ').strip()

                        try:
                            AuthService.validar_email(email)
                            break

                        except ValueError as erro:
                            print(f'[red]{erro}')


                    while True:
                        senha = InputValidator.impedir_vazio('Informe a sua senha: ')

                        try:
                            AuthService.validar_senha(senha)
                            break

                        except ValueError as erro:
                            print(f'[red]{erro}')

                    try:
                        usuario = AuthService.registrar(
                            nome,
                            email,
                            senha
                        )
                        print('[green]Cadastro realizado!')

                    except ValueError as erro:
                        print(f'[red]{erro}')




                case 3:
                    exit()

                case _:
                    print('[red]ERRO! Escolha uma opção válida!')
