import pytest
from ProjetoNivel4.services.auth_service import AuthService

def test_registrar_usuario():

    usuario = AuthService.registrar(
        "João",
        "joao@email.com",
        "Senha123"
    )

    assert usuario.nome == "João"

    assert usuario.email == (
        "joao@email.com"
    )

    assert usuario.senha_hash != (
        "Senha123"
    )


def test_senha_curta():

    with pytest.raises(ValueError):

        AuthService.validar_senha("123")


def test_senha_valida():

    AuthService.validar_senha("Senha123")


def test_senha_sem_numero():

    with pytest.raises(ValueError):

        AuthService.validar_senha("SenhaTeste")


def test_senha_sem_maiuscula():

    with pytest.raises(ValueError):

        AuthService.validar_senha(
            "senha123"
        )


def test_senha_sem_minuscula():

    with pytest.raises(ValueError):

        AuthService.validar_senha(
            "SENHA123"
        )

