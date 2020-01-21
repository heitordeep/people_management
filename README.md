# API Rest - Jobs

## App para CRUD de Jobs - usando Python 3.7.3, Django 3.0, Django Rest Framework 3.11 e SQLite 3

Antes de iniciar o app, é necessário realizar a criação de uma VirtualEnv com Python 3.7.3. Neste exemplo, estou utilizando o Pyenv.

## Siga as instruções da inicialização: 

1) Instale primeiramente os requisitos do projeto Jobs:

    ```shell
    $ make requirements
    ```

2) Após, realize a migração do BD:

    ```shell
    $ make migrate_db
    ```

3) Agora, só rodar o APP:

    ```shel
    $ make runserver
    ```

4) Não vamos esquecer de criar o super usuário do painel Admin do Django:

    ```shell
    $ make superuser
    ```


# Curl:

Na API é possível realizar todas as requisições (GET, POST, PUT, PATCH e DELETE).

# Siga as URLS de requisições:

- GET:
    ``` http://127.0.0.1:8000/api/jobs/ ```. Obter todas as vagas disponíveis. Só será retornado vagas ativas.
    ``` http://127.0.0.1:8000/api/jobs/persons/ ```. Obter todas as pessoas cadastradas nas vagas.


    ```shell
    $ curl -i http://127.0.0.1:8000/api/jobs/
    ```

    ```
        HTTP/1.1 200 OK
        Date: Mon, 20 Jan 2020 22:47:22 GMT
        Server: WSGIServer/0.2 CPython/3.7.3
        Content-Type: application/json
        Vary: Accept, Cookie
        Allow: GET, POST, HEAD, OPTIONS
        X-Frame-Options: DENY
        Content-Length: 711
        X-Content-Type-Options: nosniff

        [
            {
                "id": 1,
                "name": "Agente de Atendimento",
                "descripion": "Lorem Ipsum is simply dummy text of the printing and typesetting industry",
                "status": true,
                "salary": "900.00",
                "company": {
                    "id": 1,
                    "name": "Teleperformance"
                },
                "created_at": "2020-01-20 - 19:04:29."
            },

             {
                "id": 2,
                "name": "Programador Python",
                "descripion": "Lorem Ipsum is simply dummy text of the printing and typesetting industry",
                "status": true,
                "salary": "5000.90",
                "company": {
                    "id": 2,
                    "name": "TecNerd"
                },
                "created_at": "2020-01-20 - 19:04:29."
            },

            {
                "id": 8,
                "name": "Agente de Atendimento CHAT",
                "descripion": "Lorem Ipsum is simply dummy text of the printing and typesetting industry",
                "status": true,
                "salary": "1000.00",
                "company": {
                    "id": 1,
                    "name": "Teleperformance"
                },
                "created_at": "2020-01-20 - 19:59:10."
            }
        ]

    ```

Também é possível realizar buscas em case insensitive ou por ID:

    ```shell
    $ curl http://127.0.0.1:8000/api/jobs/?search=atendimento
    ```

    ```
        [
            {
                "id": 1,
                "name": "Agente de Atendimento",
                "descripion": "Lorem Ipsum is simply dummy text of the printing and typesetting industry",
                "status": true,
                "salary": "900.00",
                "company": {
                    "id": 1,
                    "name": "Teleperformance"
                },
                "created_at": "2020-01-20 - 19:04:29."
            },
            {
                "id": 8,
                "name": "Agente de Atendimento CHAT",
                "descripion": "Lorem Ipsum is simply dummy text of the printing and typesetting industry",
                "status": true,
                "salary": "1000.00",
                "company": {
                    "id": 1,
                    "name": "Teleperformance"
                },
                "created_at": "2020-01-20 - 19:59:10."
            }
        ]

    ```

    ```shell
    $ curl http://127.0.0.1:8000/api/jobs/1/
    ```

    ```
        [
            {
                "id": 1,
                "name": "Agente de Atendimento",
                "descripion": "Lorem Ipsum is simply dummy text of the printing and typesetting industry",
                "status": true,
                "salary": "900.00",
                "company": {
                    "id": 1,
                    "name": "Teleperformance"
                },
                "created_at": "2020-01-20 - 19:04:29."
            }
        ]
    ```


Buscar pessoas cadastradas e vagas selecionadas:

    ```shell
    $ curl -i http://127.0.0.1:8000/api/jobs/persons/
    ```

    ```
        HTTP/1.1 200 OK
        Date: Mon, 20 Jan 2020 23:05:14 GMT
        Server: WSGIServer/0.2 CPython/3.7.3
        Content-Type: application/json
        Vary: Accept, Cookie
        Allow: GET, POST, HEAD, OPTIONS
        X-Frame-Options: DENY
        Content-Length: 2077
        X-Content-Type-Options: nosniff

        [
            {
                "id": 2,
                "name": "Rafaela da Silva Oliveira",
                "email": "rafa_olive2020@gmail.com",
                "phone": "(13) 98000-4873",
                "status": true,
                "bio": "Lorem Ipsum is simply dummy text of the printing and typesetting industry",
                "jobs": [
                    {
                        "id": 1,
                        "name": "Agente de Atendimento",
                        "descripion": "Lorem Ipsum is simply dummy text of the printing and typesetting industry",
                        "status": true,
                        "salary": "900.00",
                        "company": 1,
                        "created_at": "2020-01-20 - 19:04:29."
                    },
                    {
                        "id": 2,
                        "name": "Programador Python",
                        "descripion": "Lorem Ipsum is simply dummy text of the printing and typesetting industry",
                        "status": true,
                        "salary": "5000.90",
                        "company": {
                            "id": 2,
                            "name": "TecNerd"
                        },
                        "created_at": "2020-01-20 - 19:04:29."
                    }
            }
        ]
    ```  
 
 Também é possível realizar busca case insensitive, basta utilizar o ```?search=``` no final da URL.

- POST

Cadastrar jobs:

    ```shell
    $ curl -iX POST -H "Content-Type: application/json" -d '{"name": "Programador Java", "descripion": "Lorem Ipsum", "status": true, "salary": "4000.00"}' http://127.0.0.1:8000/api/jobs/
    ```

    ```
        HTTP/1.1 201 Created
        Date: Mon, 20 Jan 2020 23:11:11 GMT
        Server: WSGIServer/0.2 CPython/3.7.3
        Content-Type: application/json
        Vary: Accept, Cookie
        Allow: GET, POST, HEAD, OPTIONS
        X-Frame-Options: DENY
        Content-Length: 148
        X-Content-Type-Options: nosniff

        
        {"id": 10, "name": "Programador Java", "descripion": "Lorem Ipsum", "status": true, "salary": "4000.00", "company": null, "created_at": "2020-01-20 - 20:11:11."}
    ```

Cadastrar pessoas:

    ```shell
    $ curl -iX POST -H "Content-Type: application/json" -d '{"name": "Fernando Heitor", "email": "heitor.aguia@gmail.com", "status": true, "phone": "(11) 98600-4400", "bio": "Lorem Ipsum is simply"}' http://127.0.0.1:8000/api/jobs/persons/
    ```

    ```
        HTTP/1.1 201 Created
        Date: Mon, 20 Jan 2020 23:17:17 GMT
        Server: WSGIServer/0.2 CPython/3.7.3
        Content-Type: application/json
        Vary: Accept, Cookie
        Allow: GET, POST, HEAD, OPTIONS
        X-Frame-Options: DENY
        Content-Length: 146
        X-Content-Type-Options: nosniff


        {"id": 5, "name": "Fernando Heitor", "email": "heitor.aguia@gmail.com", "phone": "(11) 98600-4400", "status": true,"bio": "Lorem Ipsum is simply", "jobs": []}

    ```

- Delete

Deletar jobs:

    ```shell
    $ curl -iX DELETE http://127.0.0.1:8000/api/jobs/1/
    ```

    ```
        HTTP/1.1 204 No Content
        Date: Mon, 20 Jan 2020 23:20:11 GMT
        Server: WSGIServer/0.2 CPython/3.7.3
        Vary: Accept, Cookie
        Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
        X-Frame-Options: DENY
        Content-Length: 0
        X-Content-Type-Options: nosniff

    ```

Deletar pessoas:

    ```shell
    $ curl -iX DELETE http://127.0.0.1:8000/api/jobs/person/1/
    ```

    ```
        HTTP/1.1 204 No Content
        Date: Mon, 20 Jan 2020 23:23:24 GMT
        Server: WSGIServer/0.2 CPython/3.7.3
        Vary: Accept, Cookie
        Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
        X-Frame-Options: DENY
        Content-Length: 0
        X-Content-Type-Options: nosniff

    ```


- PATCH / PUT

Atualizar por Primary Key - jobs:

    ```shell
    $ curl -iX PATCH -H "Content-Type: application/json" -d '{"name": "Programador GO", "descripion": "Vagas de
    Programador GO", "salary": "9000.00"}' http://127.0.0.1:8000/api/jobs/2/
    ```

    ```
        HTTP/1.1 200 OK
        Date: Mon, 20 Jan 2020 23:34:48 GMT
        Server: WSGIServer/0.2 CPython/3.7.3
        Content-Type: application/json
        Vary: Accept, Cookie
        Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
        X-Frame-Options: DENY
        Content-Length: 154
        X-Content-Type-Options: nosniff
    
        {"id":2,"name":"Programador GO","descripion":"Vagas de Programador GO","status":true,"salary":"9000.00","company":2,"created_at":"2020-01-20 - 19:04:41."}
    ```


Atualizar por Primary Key - pessoas:

    ```shell
    $ curl -iX PATCH -H "Content-Type: application/json" -d '{"phone": "(13) 4003-9022", "bio": "Experiência comprovada em suporte técnico nível II", "jobs": [2,4]}' http://127.0.0.1:8000/api/jobs/person/2/
    ```

    ```
        HTTP/1.1 200 OK
        Date: Mon, 20 Jan 2020 23:52:09 GMT
        Server: WSGIServer/0.2 CPython/3.7.3
        Content-Type: application/json
        Vary: Accept, Cookie
        Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
        X-Frame-Options: DENY
        Content-Length: 148
        X-Content-Type-Options: nosniff

        {"id":2,"name":"Rafaela da Silva Oliveira","email":"rafa_olive2020@gmail.com","phone":"(13) 4003-9022","status":true,"bio":"testestes","jobs":[2,4]}
    ```