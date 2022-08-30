from django.db import models

# Create your models here.


class Experience(models.Model):
    id_experience = models.AutoField(primary_key=True, null=False)
    experience_type = models.TextField(null=False)
    title = models.TextField(null=False)
    description = models.TextField(null=False)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
