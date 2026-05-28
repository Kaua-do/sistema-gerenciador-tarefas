from core.usuario import Usuario
from services.task_service import TaskService
from core.enums import (
    Prioridade,
    StatusTarefa
)
import pytest
from repositories.usuario_repository import UsuarioRepository

def fake_salvar(usuario):
    pass


def criar_usuario_fake():

    return Usuario(
        id="1",
        nome="João",
        email="joao@gmail.com",
        senha_hash="123"
    )

def test_criar_tarefa(monkeypatch):
    monkeypatch.setattr(
        UsuarioRepository,
        "salvar",
        fake_salvar
    )

    usuario = criar_usuario_fake()

    tarefa = TaskService.criar_tarefa(
        usuario,
        "Estudar",
        "Revisar OOP",
        Prioridade.ALTA
    )

    assert tarefa.titulo == "Estudar"

    assert len(
        usuario.tarefas
    ) == 1


def test_concluir_tarefa():

    usuario = criar_usuario_fake()

    tarefa = TaskService.criar_tarefa(
        usuario,
        "Estudar",
        "Python",
        Prioridade.MEDIA
    )

    TaskService.concluir_tarefa(
        usuario,
        tarefa.id
    )

    assert (
        tarefa.status
        ==
        StatusTarefa.CONCLUIDA
    )


def test_titulo_vazio():

    usuario = criar_usuario_fake()

    with pytest.raises(ValueError):

        TaskService.criar_tarefa(
            usuario,
            "",
            "Descrição",
            Prioridade.BAIXA
        )


def test_editar_tarefa(monkeypatch):
    monkeypatch.setattr(
        UsuarioRepository,
        "salvar",
        fake_salvar
    )

    usuario = criar_usuario_fake()

    tarefa = TaskService.criar_tarefa(
        usuario,
        "Antigo",
        "Descrição antiga",
        Prioridade.BAIXA
    )

    TaskService.editar_tarefa(
        usuario,
        tarefa.id,
        "Novo título",
        "Nova descrição",
        Prioridade.ALTA,
        None
    )

    assert (
        tarefa.titulo
        ==
        "Novo título"
    )

    assert (
        tarefa.prioridade
        ==
        Prioridade.ALTA
    )

def test_remover_tarefa(monkeypatch):

    monkeypatch.setattr(
        UsuarioRepository,
        "salvar",
        fake_salvar
    )

    usuario = criar_usuario_fake()

    tarefa = TaskService.criar_tarefa(
        usuario,
        "Estudar",
        "Python",
        Prioridade.MEDIA
    )

    TaskService.remover_tarefa(
        usuario,
        tarefa.id
    )

    assert (
        len(usuario.tarefas)
        ==
        0
    )

def test_concluir_tarefa_inexistente(monkeypatch):

    monkeypatch.setattr(
        UsuarioRepository,
        "salvar",
        fake_salvar
    )

    usuario = criar_usuario_fake()

    with pytest.raises(ValueError):

        TaskService.concluir_tarefa(
            usuario,
            "id_fake"
        )

def test_editar_tarefa_inexistente(monkeypatch):

    monkeypatch.setattr(
        UsuarioRepository,
        "salvar",
        fake_salvar
    )

    usuario = criar_usuario_fake()

    with pytest.raises(ValueError):

        TaskService.editar_tarefa(
            usuario,
            "id_fake",
            "Novo",
            "Descrição",
            Prioridade.ALTA,
            None
        )

def test_remover_tarefa_inexistente(monkeypatch):

    monkeypatch.setattr(
        UsuarioRepository,
        "salvar",
        fake_salvar
    )

    usuario = criar_usuario_fake()

    with pytest.raises(ValueError):

        TaskService.remover_tarefa(
            usuario,
            "id_fake"
        )

def test_buscar_por_titulo(monkeypatch):

    monkeypatch.setattr(
        UsuarioRepository,
        "salvar",
        fake_salvar
    )

    usuario = criar_usuario_fake()

    TaskService.criar_tarefa(
        usuario,
        "Estudar Python",
        "POO",
        Prioridade.ALTA
    )

    TaskService.criar_tarefa(
        usuario,
        "Jogar Minecraft",
        "Survival",
        Prioridade.MEDIA
    )

    resultado = (
        TaskService
        .buscar_por_titulo(
            usuario,
            "python"
        )
    )

    assert len(resultado) == 1

    assert (
        resultado[0].titulo
        ==
        "Estudar Python"
    )

