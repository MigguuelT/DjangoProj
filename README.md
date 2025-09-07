# Projeto Django Full-Stack

Este é um projeto Django que demonstra a integração de várias aplicações, incluindo um CRUD completo, autenticação de usuários, uma API RESTful e uma landing page.

## Funcionalidades

O projeto é dividido nas seguintes aplicações:

- **Landing_Page**: Uma página de boas-vindas simples com um formulário de contato funcional.
- **MatrizCRUD**: Uma aplicação CRUD (Criar, Ler, Atualizar, Deletar) para gerenciar um cadastro de "Clientes". Inclui paginação.
- **contato_app**: Uma aplicação para gerenciar mensagens de contato. Permite enviar, listar, editar e deletar mensagens.
- **usuarios**: Módulo de autenticação que gerencia o cadastro, login e logout de usuários, com páginas protegidas que exigem autenticação.
- **pessoas**: Uma aplicação que oferece duas interfaces para gerenciar um cadastro de "Pessoas":
    - Uma interface web tradicional (HTML/CSS/JS) com funcionalidades CRUD.
    - Uma API RESTful construída com Django REST Framework.

## Tecnologias Utilizadas

- **Backend**:
    - Python
    - Django
    - Django REST Framework (para a API)
    - Django Widget Tweaks (para facilitar a renderização de formulários)
- **Database**:
    - SQLite (para desenvolvimento)

## Pré-requisitos

- Python 3.8 ou superior
- `pip` (gerenciador de pacotes do Python)

## Instalação

Siga os passos abaixo para configurar o ambiente de desenvolvimento local.

1.  **Clone o repositório:**
    ```bash
    git clone <URL_DO_REPOSITORIO>
    cd <NOME_DO_DIRETORIO>
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Para Windows
    python -m venv venv
    venv\Scripts\activate

    # Para macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Aplique as migrações do banco de dados:**
    ```bash
    python manage.py migrate
    ```

5.  **Crie um superusuário (para acesso ao Admin):**
    ```bash
    python manage.py createsuperuser
    ```
    Siga as instruções para criar um nome de usuário, email e senha.

## Executando a Aplicação

Para iniciar o servidor de desenvolvimento, execute o comando:

```bash
python manage.py runserver
```

A aplicação estará disponível em `http://127.0.0.1:8000/`.

- A **Landing Page** é a página inicial.
- O **CRUD de Clientes** está em `/home/`.
- O **CRUD de Pessoas (HTML)** está em `/pessoas/`.
- O **Módulo de Contato** está em `/contato/`.
- As páginas de **Cadastro e Login** estão em `/usuarios/cadastro/` e `/usuarios/login/`.

## Endpoints da API

A API para o recurso `Pessoa` está disponível no prefixo `/api/`. Ela oferece os seguintes endpoints:

- `GET /api/pessoas/`: Lista todas as pessoas.
- `POST /api/pessoas/`: Cria uma nova pessoa.
- `GET /api/pessoas/{id}/`: Retorna os detalhes de uma pessoa específica.
- `PUT /api/pessoas/{id}/`: Atualiza os dados de uma pessoa.
- `PATCH /api/pessoas/{id}/`: Atualiza parcialmente os dados de uma pessoa.
- `DELETE /api/pessoas/{id}/`: Deleta uma pessoa.

**Exemplo de corpo para POST/PUT:**
```json
{
    "nome": "João da Silva",
    "idade": 30
}
```
