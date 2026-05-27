from rich import print

class MenuView:

    @staticmethod
    def menu_tarefas():
        print("[blue]1 - Criar tarefa")
        print("[blue]2 - Listar todas")
        print("[blue]3 - Filtrar tarefas")
        print("[blue]4 - Buscar por título")
        print("[blue]5 - Concluir tarefa")
        print("[blue]6 - Editar tarefa")
        print("[blue]7 - Remover tarefa")
        print("[blue]8 - Exportar tarefa")
        print("[blue]9 - Logout")


    @staticmethod
    def menu_filtro():
        print("-" * 30)
        print("[blue]1 - Pendentes")
        print("[blue]2 - Concluídas")
        print("[blue]3 - Prioridade")
        print("[blue]4 - Prazo")
        print("[blue]5 - Vencidas")
        print("[blue]6 - Voltar")
        print("-" * 30)


    @staticmethod
    def menu_exportacao():
        print("-" * 30)
        print("[blue]1 - Exportar em TXT")
        print("[blue]2 - Exportar em CSV")
        print("[blue]3 - Exportar em JSON")
        print("-" * 30)

