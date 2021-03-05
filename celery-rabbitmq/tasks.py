from celery import Celery
from time import sleep

app = Celery("tasks", broker="amqp://admin:admin@localhost:8888",
             backend="amqp://admin:admin@localhost:8888")


@app.task
def reverse(text):
    print("reverse task")
    sleep(5)
    return text[::-1]
