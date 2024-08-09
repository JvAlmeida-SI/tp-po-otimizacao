## Instalação

1. Clone o repositório para sua máquina local:

    ```bash
    git clone https://github.com/JvAlmeida-SI/tp-po-otimizacao.git
    ```

2. Crie um ambiente virtual para o projeto:

    ```bash
    python -m venv venv
    ```

3. Ative o ambiente virtual:

    - No Windows:

        ```bash
        venv\Scripts\activate
        ```

    - No macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4. Instale as dependências do projeto usando o arquivo `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

## Inicialização do Projeto

1. Aplique as migrações do banco de dados:

    ```bash
    python manage.py migrate
    ```

2. Crie um superusuário para acessar o admin do Django:

    ```bash
    python manage.py createsuperuser
    ```

3. Inicie o servidor de desenvolvimento:

    ```bash
    cd OtimizacaoSistema
    python manage.py runserver
    ```

4. Acesse o projeto no navegador através do endereço:

    ```bash
    http://127.0.0.1:8000/
    ```
