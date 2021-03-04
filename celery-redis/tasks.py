from celery_app import app


@app.task
def multiply(a, b):
    return a * b
