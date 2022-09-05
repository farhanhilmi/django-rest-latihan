from django.db import models

# Create your models here.


class ExperienceType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(null=False)


class Experience(models.Model):
    id_experience = models.AutoField(primary_key=True, null=False)
    # experience_type = models.TextField(null=False)
    experience_type = models.ForeignKey(
        ExperienceType, on_delete=models.CASCADE)
    title = models.TextField(null=False)
    description = models.TextField(null=False)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
