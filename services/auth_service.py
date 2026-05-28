from repositories.usuario_repository import UsuarioRepository
from core.usuario import Usuario
from uuid import uuid4
import bcrypt

class AuthService:

    @classmethod
    def validar_nome(cls, nome):
        if not nome.strip():
            raise ValueError(
                "Nome inválido!"
            )

        if len(nome) < 3:
            raise ValueError(
                "Nome muito curto"
            )

    @classmethod
    def validar_email(cls, email):

        if "@" not in email:
            raise ValueError(
                "Formato de email inválido!"
            )

        usuario = UsuarioRepository.buscar_por_email(email)

        if usuario:
            raise ValueError(
                "Esse e-mail já existe!"
            )


    @classmethod
    def validar_senha(cls, senha):
        if len(senha) < 6:
            raise ValueError(
                "Senha muito curta"
            )

        if len(senha) > 20:
            raise ValueError(
                "Senha muito longa"
            )

        tem_letra = any(c.isalpha() for c in senha)

        if not tem_letra:

            raise ValueError(
                "Senha precisa ter ao menos 1 letra"
            )

        tem_numero = any(c.isdigit() for c in senha)

        if not tem_numero:

            raise ValueError(
                "Senha precisa ter ao menos 1 numero"
            )

        tem_maiuscula = any(c.isupper() for c in senha)

        if not tem_maiuscula:
            raise ValueError(
                "Senha precisa ter ao menos 1 letra maiuscula"
            )

        tem_minuscula =  any(c.islower() for c in senha)

        if not tem_minuscula:
            raise ValueError(
                "Senha precisa ter ao menos 1 letra minuscula"
            )

    @classmethod
    def registrar(cls, nome, email, senha):

        cls.validar_email(email)
        cls.validar_senha(senha)

        usuario_id = str(uuid4())

        senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt()).decode()

        usuario = Usuario(usuario_id, nome, email, senha_hash)

        UsuarioRepository.salvar(usuario)

        return usuario


    @classmethod
    def login(cls, email, senha):

        usuario_logado = UsuarioRepository.buscar_por_email(email)

        if not usuario_logado:
            raise ValueError(
                'Credenciais inválidas!'
            )

        senha_correta = bcrypt.checkpw(senha.encode(), usuario_logado.senha_hash.encode())

        if not senha_correta:
            raise ValueError(
                "Senha incorreta!"
            )

        return usuario_logado
