from tasks import app

app.send_task("tasks.reverse", args=["1234"])
