from rich import print
from validators.input_validator import InputValidator
from views.task_view import TaskView
from services.task_service import TaskService
from services.logger_service import LoggerService
from core.enums import (Prioridade)
from views.menuview import MenuView


class TaskMenu:
    def __init__(self, usuario):
        self.usuario = usuario

    def ler_prioridade(self):
        while True:
            try:
                return Prioridade(
                    InputValidator.ler_int(
                        "Digite prioridade 1-Baixa 2-Média 3-Alta: "
                    )
                )

            except ValueError:
                TaskView.mostrar_erro(
                    "Prioridade inválida!"
                )


    def criar_tarefa(self):
        try:

            titulo = input("Escreva o título: ")

            descricao = input("Escreva a descrição (Enter para pular): ")

            while True:

                try:
                    prioridade = self.ler_prioridade()

                    prioridade = Prioridade(prioridade)

                    break

                except ValueError:
                    print("[red]Prioridade inválida!")

            prazo = InputValidator.ler_data("Digite o prazo (DD/MM/AAAA) ou Enter para ignorar: ")

            tarefa = TaskService.criar_tarefa(self.usuario, titulo, descricao, prioridade, prazo)

            LoggerService.log(
                usuario=self.usuario.email,
                acao="CRIOU",
                detalhe=tarefa.titulo
            )

            print(
                f"[green]Tarefa "
                f"'{tarefa.titulo}' "
                f"criada!"
            )

        except ValueError as erro:
            TaskView.mostrar_erro(erro)

    def listar_tarefas(self):

        if not self.usuario.tarefas:
            print("[yellow]Nenhuma tarefa encontrada!")

            return

        TaskView.mostrar_tarefas(
            self.usuario.tarefas
        )

    def listar_pendentes(self):

        tarefas = TaskService.listar_pendentes(self.usuario)

        if not tarefas:
            print(
                "Sem tarefas pendentes!"
            )

        TaskView.mostrar_tarefas(tarefas)

    def listar_concluidas(self):
        tarefas = TaskService.listar_concluidas(self.usuario)

        if not tarefas:
            print(
                "Sem tarefas concluídas!"
            )

        TaskView.mostrar_tarefas(tarefas)


    def listar_por_prioridade(self):
        tarefas = TaskService.ordenar_por_prioridade(self.usuario)

        if not tarefas:
            print(
                "Sem tarefas com prioridade!"
            )

        TaskView.mostrar_tarefas(tarefas)


    def listar_por_prazo(self):
        tarefas = TaskService.ordenar_por_prazo(self.usuario)

        if not tarefas:
            print(
                "Sem tarefas com prazo!"
            )

        TaskView.mostrar_tarefas(tarefas)


    def tarefas_vencidas(self):
        tarefas = TaskService.tarefas_vencidas(self.usuario)

        if not tarefas:
            print(
                "[yellow]Sem tarefas vencidas!"
            )
            return

        TaskView.mostrar_tarefas(tarefas)


    def buscar_por_titulo(self):
        texto = input("Buscar título: ")

        tarefas = TaskService.buscar_por_titulo(self.usuario, texto)

        if not tarefas:
            print("[yellow]Nenhuma tarefa encontrada!")
            return

        TaskView.mostrar_tarefas(tarefas)

    def concluir_tarefa(self):
        try:
            tarefa_id = input("Digite o ID da tarefa: ")

            TaskService.concluir_tarefa(self.usuario, tarefa_id)

            LoggerService.log(
                usuario=self.usuario.email,
                acao="CONCLUIU",
                detalhe=tarefa_id
            )
            TaskView.mostrar_sucesso(f"Tarefa concluída!")

        except ValueError as erro:
            TaskView.mostrar_erro(erro)


    def editar_tarefa(self):
        try:
            tarefa_id = input("Digite o ID da tarefa: ")

            tarefa = TaskService.obter_tarefa(self.usuario, tarefa_id)

            if not tarefa:
                raise ValueError(
                    "Tarefa não encontrada!"
                )

            novo_titulo = input(f"Novo título (Enter mantém atual): ")

            if not novo_titulo:
                novo_titulo = tarefa.titulo

            nova_descricao = input(f"Nova descrição (Enter mantém atual): ")

            if not nova_descricao:
                nova_descricao = tarefa.descricao

            prazo_atual = (
                tarefa.prazo.strftime("%d/%m/%Y")
                if tarefa.prazo
                else "Sem prazo"
            )

            novo_prazo = InputValidator.ler_data(f"Novo prazo (DD/MM/AAAA) (Enter mantém atual): ")

            while True:

                try:
                    nova_prioridade = Prioridade(InputValidator.ler_int("Digite a nova prioridade 1-Baixa 2-Média 3-Alta (Enter mantém atual): "))
                    break

                except ValueError:
                    TaskView.mostrar_erro("Prioridade inválida!")

            TaskService.editar_tarefa(self.usuario, tarefa_id, novo_titulo, nova_descricao, nova_prioridade, novo_prazo)

            LoggerService.log(
                usuario=self.usuario.email,
                acao="EDITOU",
                detalhe=tarefa.titulo
            )
            TaskView.mostrar_sucesso(f"Tarefa editada!")

        except ValueError as erro:
            TaskView.mostrar_erro(erro)


    def remover_tarefa(self):
        try:
            tarefa_id = input("Digite o ID da tarefa: ")

            confirmar = InputValidator.confirmar("Deseja realmente remover a tarefa? (S/N): ")

            if not confirmar:
                print("[yellow]Operação cancelada!")
                return

            TaskService.remover_tarefa(self.usuario, tarefa_id)

            LoggerService.log(
                usuario=self.usuario.email,
                acao="REMOVEU",
                detalhe=tarefa_id
            )

            TaskView.mostrar_sucesso(f"Tarefa removida!")

        except ValueError as erro:
            TaskView.mostrar_erro(erro)

    def exportar_txt(self):

        caminho = TaskService.exportar_txt(self.usuario)

        TaskView.mostrar_sucesso(f"Arquivo exportado em: {caminho}")


    def exportar_csv(self):

        caminho = TaskService.exportar_csv(self.usuario)

        TaskView.mostrar_sucesso(f"CSV exportado em: {caminho}")

    def exportar_json(self):

        caminho = TaskService.exportar_json(self.usuario)

        TaskView.mostrar_sucesso(f"JSON exportado em: {caminho}")

    def menu_exportar_tarefa(self):
        while True:

            MenuView.menu_exportacao()

            opcao = InputValidator.ler_int("Escolha sua opção: ")

            match opcao:
                case 1:
                    self.exportar_txt()

                case 2:
                    self.exportar_csv()

                case 3:
                    self.exportar_json()

                case _:
                    print("Opção inválida!")








    def menu_filtros(self):
        while True:

            MenuView.menu_filtro()

            opcao = InputValidator.ler_int("Escolha sua opção: ")

            match opcao:
                case 1:
                    self.listar_pendentes()
                case 2:
                    self.listar_concluidas()
                case 3:
                    self.listar_por_prioridade()
                case 4:
                    self.listar_por_prazo()
                case 5:
                    self.tarefas_vencidas()
                case 6:
                    break
                case _:
                    print("Opção inválida!")



    def mostrar_menu(self):

        while True:

            dados = TaskService.dashboard(self.usuario)

            TaskView.mostrar_dashboard(self.usuario, dados)

            MenuView.menu_tarefas()

            opcao = InputValidator.ler_int("Escolha uma opcao: ")

            match opcao:

                case 1:
                    self.criar_tarefa()

                case 2:
                    self.listar_tarefas()

                case 3:
                    self.menu_filtros()

                case 4:
                    self.buscar_por_titulo()

                case 5:
                    self.concluir_tarefa()

                case 6:
                    self.editar_tarefa()

                case 7:
                    self.remover_tarefa()

                case 8:
                    self.menu_exportar_tarefa()

                case 9:
                    confirmar = InputValidator.confirmar("Tem certeza que deseja sair? (S/N): ")

                    if not confirmar:
                        continue

                    break

                case _:
                    print("[red]ERRO! Escolha uma opcao válida!")


