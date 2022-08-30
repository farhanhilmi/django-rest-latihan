from django.db import models

from utils.helper import randomFileName

# Create your models here.


# def fileName(instance, filename):
#     return '/'.join(['images', str(instance.title), filename])


class Book(models.Model):
    id_book = models.AutoField(primary_key=True)
    title = models.TextField(null=False)
    author = models.TextField(null=False)
    description = models.TextField(null=False)
    image = models.ImageField(null=False, upload_to=randomFileName('books'))
