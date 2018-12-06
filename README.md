# Django-Polls

## O que é?

API Rest para criar, editar e deletar enquetes usando Python/Django.


## Ferramentas utilizadas

Django Rest Framework para API Rest
Swagger para a documentação
Heroku para deploy
CircleCI para integração contínua


## Configurando o ambiente e rodando a aplicação

Com python 3.6 ou superior instalado crie e ative um ambiente virtual
```
python3.6 -m venv venv
source venv/bin/activate
```

Clonar o repositório
```
git clone https://github.com/tapumar/Django-Polls.git
cd Django-Polls
```

Depois deve-se instalar os pacotes contidos no `requirements.txt` com
```
pip install -r requirements.txt
```

Para rodar a aplicação basta digitar o comando
```
./manage.py runserver
```


## End-Points da API Rest

/api/polls retorna as enquetes existentes com suas respectivas escolhas
/api/polls/<pk> retorna a enquete especificada pela pk
/api/polls/<pk>  deleta a enquete especificada pela pk
/api/polls/<question_pk>/choices/<choice_pk>/vote salva o voto na
