from invoke import task

@task
def runserver(context):
    context.run("pipenv run python manage.py runserver 0.0.0.0:8000")

@task
def sass(context):
    context.run("sass --watch --poll static/scss/:static/css")