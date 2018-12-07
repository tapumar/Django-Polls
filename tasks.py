from invoke import task


@task
def run(c):
    """ Run Django app """
    c.run('python manage.py runserver')


@task
def migrate(c):
    """ Make migrations """
    c.run("python manage.py makemigrations")
    c.run("python manage.py migrate")


@task
def travis(c):
    """ Test Django app """
    c.run("python manage.py test")


@task
def style(c):
    """ Check if Django app is following PEP8 recommendations """
    c.run("pycodestyle polls/. teste_django/. tasks.py "
          "--exclude=migrations,settings.py")


@task
def install(c):
    """ Install Django app's requirements """
    c.run("pip install -r requirements.txt")
