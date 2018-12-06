from invoke import task


@task
def run(c):
    """ Run Django app """
    c.run('django-admin runserver --settings=teste_django.settings')


@task
def migrate(c):
    """ Make migrations """
    c.run("python manage.py makemigrations")
    c.run("python manage.py migrate")


@task
def travis(c):
    c.run("python manage.py test")


@task
def test(c):
    """ Test Django app """
    c.run("python manage.py test --testrunner=green.djangorunner.DjangoRunner")


@task
def style(c):
    c.run("pycodestyle polls/. teste_django/. tasks.py "
          "--exclude=migrations,settings.py")


@task
def install(c):
    c.run("pip install -r requirements.txt")
