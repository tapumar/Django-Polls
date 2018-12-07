# Django-Polls

## O que é?

API Rest para criar, editar e deletar enquetes usando Python/Django.


## Ferramentas utilizadas

- Django Rest Framework para API Rest
- Swagger para a documentação
- Heroku para deploy
- TravisCI para integração contínua

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
ou
```
inv run
```

<<<<<<< HEAD
Abrir a aplicação  e ver a lista de polls e votar
```
http://127.0.0.1:8000/polls
```

=======
>>>>>>> ef55cfc89c0574bfba9d8b222cd7f478ef105f85
Para rodar os testes
```
./manage.py test
```



## End-Points da API Rest
```
/api/polls retorna as enquetes existentes com suas respectivas escolhas
```
```
/api/polls/<pk> retorna a enquete especificada pela pk
```
```
/api/polls/<question_pk>/choices/<choice_pk>/vote salva o voto
```
