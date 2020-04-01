from config.tasks import app
from .models import Post


@app.task
def minus(x, y):
    return x - y


@app.task
def test_save(n):
    for i in range(n):
        title = 'test' + str(i)
        Post(title=title).save()

