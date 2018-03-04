# Introdução

Este projeto é uma API com controle de notas por usuario, possibilitando a listagem, criação, edição e exlusão das mesmas.

Também contém um módulo de controle de usuário. Possibilitando criar um usuário, logar e deslogar da sessão.

## Tecnologias utilizadas:
* Django 2
* Django Rest Framework


### 1. Instalação

Com sua virtualenv ativada instale:

```sh
(env) $ pip install -r requirements.txt
```


### 2. Atualizando banco

```sh
(env) $ python manage.py makemigrations
(env) $ python manage.py migrate
```


### 3. Criando um usuário admin

```sh
(env) $ python manage.py createsuperuser
```


### 4. Rodando o projeto
```sh
(env) $ python3 manage.py runserver
```

# Explorando API

### 1. '/api/'
  URL responsável por listar os endpoints disponíveis na API.


### 2. '/api/accounts/'
  URL responsável por possibilitar a criação (através do método POST do HTTP) de um usuário NÃO ADMIN, caso algum usuário NÃO estiver em sessão.

### 3. '/admin/'
Mostra a parte do admin já implementada pelo django. Somente usuários ADMIN conseguem acessa-los. O usuário criado em '/api/accounts/' NÃO É ADMIN.

### 4. '/notas/'
URL responsável por possibilitar a listagem (GET) e criação (POST) das notas do usuário logado na sessão.

### 5. '/notas/< pk >'
URL responsável por possibilitar editar (PUT) e excluir (DELETE) a nota do usuário pelo id, caso ela já exista.  
