from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(u'標題', max_length=50)
    author = models.CharField(u'作者', max_length=10)
    content = models.CharField(u'內文', max_length=2000)
    post_date = models.DateTimeField(u'發佈時間',auto_now_add=True)

    class Meta:
        ordering = ['-post_date']