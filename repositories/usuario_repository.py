import json
from pathlib import Path
from ProjetoNivel4.core.usuario import Usuario

class UsuarioRepository:

    ARQUIVO = Path("save/usuarios.json")

    @classmethod
    def criar_arquivo(cls):

        usuarios = {
            "usuarios": []
        }

        if not cls.ARQUIVO.exists():

            cls.ARQUIVO.parent.mkdir(exist_ok=True)

            with open(cls.ARQUIVO, 'w', encoding='utf-8') as arquivo:

                json.dump(usuarios, arquivo, ensure_ascii=False, indent=4)


    @classmethod
    def salvar_seguro(cls, caminho, dados):
        arquivo_temp = (str(caminho)) + ".tmp"

        with open(arquivo_temp, 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)

        Path(arquivo_temp).replace(Path(caminho))


    @classmethod
    def salvar(cls, usuario: Usuario):

        cls.criar_arquivo()

        lista = cls.carregar()

        achou = False

        for i, u in enumerate(lista):

            if u.id == usuario.id:

                lista[i] = usuario

                achou = True

                break

        if not achou:

            lista.append(usuario)


        dados_novos = {
            "usuarios": [usuario.to_dict() for usuario in lista]
        }

        cls.salvar_seguro(cls.ARQUIVO, dados_novos)


    @classmethod
    def carregar(cls) -> list[Usuario]:

        cls.criar_arquivo()

        with open(cls.ARQUIVO, 'r', encoding='utf-8') as arquivo:

            dados = json.load(arquivo)

            lista = [Usuario.from_dict(usuario) for usuario in dados["usuarios"]]

            return lista


    @classmethod
    def buscar_por_email(cls, email:str) -> Usuario | None:

        usuarios = cls.carregar()

        for usuario in usuarios:

            if usuario.email == email:

                return usuario

        return None


    @classmethod
    def buscar_por_id(cls, id:str) -> Usuario | None:

        usuarios = cls.carregar()

        for usuario in usuarios:

            if usuario.id == id:

                return usuario

        return None




