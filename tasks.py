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
def test(c):
    """ Test Django app """
    c.run("python manage.py test --testrunner=green.djangorunner.DjangoRunner")


@task
def style(c):
    c.run("pycodestyle poll/. pollapp/. tasks.py "
          "--exclude=migrations,settings.py")


@task()
def install(c):
    c.run("pip install -r requirements.txt")
