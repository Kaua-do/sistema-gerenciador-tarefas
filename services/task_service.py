from datetime import datetime
from core.tarefa import Tarefa
from core.usuario import Usuario
from core.enums import *
from uuid import uuid4
import os
import csv
import json
from repositories.usuario_repository import UsuarioRepository


class TaskService:
    @classmethod
    def obter_tarefa(cls, usuario, tarefa_id):
        if not usuario:
            raise ValueError(
                "Usuário inválido!"
            )

        tarefa = usuario.buscar_tarefa(tarefa_id)

        if not tarefa:
            raise ValueError(
                "TArefa não encontrada!"
            )

        return tarefa


    @classmethod
    def dashboard(cls, usuario):
        if not usuario:
            raise ValueError(
                "Usuário inválido!"
            )

        total = len(usuario.tarefas)

        pendentes = len(cls.listar_pendentes(usuario))

        concluidas = len(cls.listar_concluidas(usuario))

        vencidas = len(cls.tarefas_vencidas(usuario))

        alta_prioridade = sum(
            tarefa.prioridade == Prioridade.ALTA
            for tarefa in usuario.tarefas
        )

        return {
            "total": total,
            "pendentes": pendentes,
            "concluidas": concluidas,
            "vencidas": vencidas,
            "alta_prioridade": alta_prioridade
        }

    @classmethod
    def listar_pendentes(cls, usuario):
        if not usuario:
            raise ValueError(
                "Usuário inválido!"
            )

        return [
            tarefa for tarefa in usuario.tarefas
            if tarefa.status == StatusTarefa.PENDENTE
        ]

    @classmethod
    def listar_concluidas(cls, usuario):
        if not usuario:
            raise ValueError(
                "Usuário inválido!"
            )

        return [
            tarefa for tarefa in usuario.tarefas
            if tarefa.status == StatusTarefa.CONCLUIDA
        ]

    @classmethod
    def ordenar_por_prioridade(cls, usuario):
        if not usuario:
            raise ValueError(
                "Usuário inválido!"
            )

        return sorted(usuario.tarefas, key=lambda tarefa: tarefa.prioridade.value, reverse=True)


    @classmethod
    def ordenar_por_prazo(cls, usuario):
        if not usuario:
            raise ValueError(
                "Usuário inválido!"
            )

        return sorted(usuario.tarefas, key=lambda tarefa: tarefa.prazo or datetime.max)


    @classmethod
    def buscar_por_titulo(cls, usuario, titulo):
        if not usuario:
            raise ValueError(
                "Usuário inválido!"
            )

        return [
            tarefa for tarefa in usuario.tarefas
            if titulo.lower() in tarefa.titulo.lower()
        ]

    @classmethod
    def tarefas_vencidas(cls, usuario):
        if not usuario:
            raise ValueError(
                "Usuário inválido!"
            )

        agora = datetime.now().date()

        return [
            tarefa for tarefa in usuario.tarefas
            if tarefa.prazo
            and tarefa.prazo.date() < agora
               and tarefa.status != StatusTarefa.CONCLUIDA
        ]





    @classmethod
    def criar_tarefa(cls, usuario: Usuario, titulo: str, descricao: str, prioridade, prazo=None) -> Tarefa:
        if not usuario:
            raise ValueError(
                "Usuário inválido!"
            )

        if not titulo.strip():

            raise ValueError(
                "Título inválido"
            )

        tarefa = Tarefa(id=str(uuid4())[:6], titulo=titulo, descricao=descricao, prioridade=prioridade, prazo=prazo)

        usuario.adicionar_tarefa(tarefa)

        UsuarioRepository.salvar(usuario)

        return tarefa


    @classmethod
    def concluir_tarefa(cls, usuario, tarefa_id):
        if not usuario:
            raise ValueError(
                "Usuário inválido!"
            )

        tarefa = usuario.buscar_tarefa(tarefa_id)

        if not tarefa:

            raise ValueError(
                'Tarefa não encontrada'
            )

        tarefa.concluir()

        UsuarioRepository.salvar(usuario)


    @classmethod
    def editar_tarefa(cls, usuario, tarefa_id, titulo, descricao, prioridade, prazo):
        if not usuario:
            raise ValueError(
                "Usuário inválido!"
            )

        tarefa = usuario.buscar_tarefa(tarefa_id)

        if not tarefa:

            raise ValueError(
                'Tarefa não encontrada'
            )

        tarefa.editar(titulo, descricao, prioridade, prazo)

        UsuarioRepository.salvar(usuario)


    @classmethod
    def remover_tarefa(cls, usuario, tarefa_id):
        if not usuario:
            raise ValueError(
                "Usuário inválido!"
            )

        tarefa = usuario.buscar_tarefa(tarefa_id)

        if not tarefa:
            raise ValueError(
                "Tarefa não encontrada"
            )

        usuario.remover_tarefa(tarefa_id)

        UsuarioRepository.salvar(usuario)


    @classmethod
    def exportar_txt(cls, usuario):
        if not usuario:
            raise ValueError(
                "Usuário inválido!"
            )

        pasta = "exports"

        os.makedirs(pasta, exist_ok=True)

        caminho = os.path.join(
            pasta,
            f"tarefas_{usuario.nome}.txt"
        )

        with open(caminho, "w", encoding="utf-8") as arquivo:

            arquivo.write(
                f"RELATÓRIO DE TAREFAS - {usuario.nome}\n"
            )

            arquivo.write("=" * 50 + "\n\n")

            if not usuario.tarefas:
                arquivo.write(
                    "Nenhuma tarefa encontrada.\n"
                )

            else:

                for tarefa in usuario.tarefas:

                    prazo = (
                        tarefa.prazo.strftime("%d/%m/%Y")
                        if tarefa.prazo
                        else "Sem prazo"
                    )

                    arquivo.write(
                        f"ID: {tarefa.id}\n"
                    )

                    arquivo.write(
                        f"Título: {tarefa.titulo}\n"
                    )

                    arquivo.write(
                        f"Descrição: {tarefa.descricao}\n"
                    )

                    arquivo.write(
                        f"Status: {tarefa.status.value}\n"
                    )

                    arquivo.write(
                        f"Prioridade: {tarefa.prioridade.value}\n"
                    )

                    arquivo.write(
                        f"Prazo: {prazo}\n"
                    )

                    arquivo.write(
                        "-" * 50 + "\n"
                    )

                return caminho

    @classmethod
    def exportar_csv(self, usuario):
        if not usuario:
            raise ValueError(
                "Usuário inválido!"
            )

        pasta = "exports"

        os.makedirs(pasta, exist_ok=True)

        caminho = os.path.join(pasta, f"tarefas_{usuario.nome}.csv")

        with open(caminho, "w", encoding="utf-8") as arquivo:

            escritor = csv.writer(arquivo)

            escritor.writerow([
                "ID",
                "Título",
                "Descrição",
                "Status",
                "Prioridade",
                "Prazo"
            ])

            for tarefa in usuario.tarefas:

                prazo = (
                    tarefa.prazo.strftime("%d/%m/%Y")
                    if tarefa.prazo
                    else "Sem prazo"
                )

                escritor.writerow([
                    tarefa.id,
                    tarefa.titulo,
                    tarefa.descricao,
                    tarefa.status.value,
                    tarefa.prioridade.value,
                    prazo
                ])

            return caminho

    @classmethod
    def exportar_json(self, usuario):

        pasta = "exports"

        os.makedirs(pasta, exist_ok=True)

        caminho = os.path.join(pasta, f"tarefas_{usuario.nome}.json")

        tarefas = [
            tarefa.to_dict() for tarefa in usuario.tarefas
        ]

        dados = {
            "usuario": usuario.nome,
            "email": usuario.email,
            "total_tarefas": len(usuario.tarefas),
            "tarefas": tarefas,
        }

        with open(caminho, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)

        return caminho



