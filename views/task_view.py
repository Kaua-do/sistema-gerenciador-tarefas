from rich import print
from rich.table import Table
from rich.panel import Panel
from ProjetoNivel4.core.enums import (
    StatusTarefa,
    Prioridade
)

class TaskView:
    @classmethod
    def mostrar_erro(self, erro):
        print(f"[red]ERRO: {erro}")


    @classmethod
    def mostrar_sucesso(cls, msg):
        print(f"[green]{msg}")


    @classmethod
    def mostrar_dashboard(self, usuario, dados):

        total = dados["total"]
        concluidas = dados["concluidas"]

        if total > 0:
            porcentagem = int((concluidas / total) * 100)
        else:
            porcentagem = 0

        barra = (
                "█" * (porcentagem // 10)
                + "░" * (10 - porcentagem // 10)
        )

        texto = f"""
[magenta]:bust_in_silhouette: Usuário: {usuario.nome}

[blue]:pushpin: Total: {dados["total"]}
[green]:green_circle: Concluídas: {dados["concluidas"]}
[yellow]:yellow_circle: Pendentes: {dados["pendentes"]}
[red]:red_circle: Vencidas: {dados["vencidas"]}
[bright_red]:fire: Alta prioridade: {dados["alta_prioridade"]}
    
[cyan]Progresso:[/] {barra} {porcentagem}%

[bold]Legenda:[/]
[green]🟢 Baixa prioridade[/]
[yellow]🟡 Média prioridade[/]
[red]🔴 Alta prioridade[/]
"""

        print(Panel(texto, title=":bar_chart: Dashboard", border_style="blue", expand=False))

    @classmethod
    def mostrar_tarefas(self, tarefas):
        from datetime import datetime

        tabela = Table(title="Suas tarefas")

        tabela.add_column("ID", style="cyan")
        tabela.add_column("Título", style="green")
        tabela.add_column("Descrição", style="yellow")
        tabela.add_column("Status", justify="center")
        tabela.add_column("Prioridade", style="blue")
        tabela.add_column("Prazo", style="red")

        for tarefa in tarefas:

            status = (
                "[yellow]:yellow_circle: PENDENTE"
                if tarefa.status == StatusTarefa.PENDENTE
                else "[green]:green_circle: CONCLUÍDA"
            )

            agora = datetime.now()

            if not tarefa.prazo:
                prazo = "Sem prazo"

            elif tarefa.prazo < agora:
                prazo = f"[red]{tarefa.prazo.strftime('%d/%m/%Y')}"

            elif tarefa.prazo.date() == agora.date():
                prazo = f"[yellow]{tarefa.prazo.strftime('%d/%m/%Y')}"

            else:
                prazo = f"[green]{tarefa.prazo.strftime('%d/%m/%Y')}"

            prioridade = {
                Prioridade.BAIXA: "[green]:green_circle: Baixa",
                Prioridade.MEDIA: "[yellow]:yellow_circle: Média",
                Prioridade.ALTA: "[red]:red_circle: Alta"
            }[tarefa.prioridade]

            tabela.add_row(
                str(tarefa.id),
                tarefa.titulo,
                tarefa.descricao,
                status,
                prioridade,
                prazo
            )

        print(tabela)


