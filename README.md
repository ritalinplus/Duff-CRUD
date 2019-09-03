# Duff CRUD
Welcome to Duff CRUD, a easy system to manage clients IBAN accounts.

## Deploy System
To deploy the system, follow this steps:

1. Clone or Download project from https://github.com/ritalinplus/Rindus-CRUD/tree/feature/create_project_doc,
then from root project directory:  

    `docker-compose up [-d]`

2. Access using your browser to:

    `http://localhost:8000`

3. Log in using a google account. 

4. Additionally you can export a few client data:

    `cat db/backups/test_dump.sql | docker exec -i ps01 psql -U postgres` 

## Execute unit tests

`docker exec -t dg01 python manage.py test`

## Create project documentation (Sphinx)

For Windows

`./doc/make.bat html`

For Linux 

`./doc/make html`

| NOTE: Sphinx 1.5.6 and sphinx-rtd-theme 0.4.3 is needed |
| --- |

## Useful command

### Create postgres backup

`docker exec -t ps01 pg_dump -c -U postgres > test_dump.sql`


### Restore postgres backup

`cat test_dump.sql | docker exec -i ps01 psql -U postgres`
