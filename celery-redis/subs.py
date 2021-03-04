from celery_app import app

promise = app.send_task("tasks.multiply", args=[2, 2])
data = promise.get()
print(data)
