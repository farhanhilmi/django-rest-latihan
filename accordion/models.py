from django.db import models

# Create your models here.


class Accordion(models.Model):
    id_accordion = models.AutoField(primary_key=True)
    title = models.TextField(null=False)
    deskripsi = models.TextField(null=False)
