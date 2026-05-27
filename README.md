# Sistema de Gerenciamento de Tarefas

Projeto de terminal desenvolvido em Python utilizando Programação Orientada a Objetos (POO), autenticação segura com bcrypt, persistência em JSON, dashboard interativo, filtros e exportação de tarefas.

## Funcionalidades

- Cadastro e login de usuários
- Senhas criptografadas com bcrypt
- CRUD completo de tarefas
- Dashboard com estatísticas
- Filtros por:
  - pendentes
  - concluídas
  - prioridade
  - prazo
  - vencidas
- Busca por título
- Exportação para TXT, CSV e JSON
- Sistema de logs
- Testes automatizados com pytest

## Tecnologias utilizadas

- Python
- Rich
- Pytest
- Bcrypt
- JSON

## Estrutura do projeto

```txt
core/
services/
repositories/
validators/
menus/
view/
tests/
```

## Como executar

Clone o projeto:

```bash
git clone URL_DO_REPOSITORIO
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute:

```bash
python main.py
```

## Testes

Para executar os testes:

```bash
pytest
```

## Conceitos aplicados

- Programação Orientada a Objetos
- Repository Pattern
- Service Layer
- Enum
- Persistência de dados
- Criptografia de senha
- Tratamento de exceções
- Arquitetura em camadas
- Testes automatizados