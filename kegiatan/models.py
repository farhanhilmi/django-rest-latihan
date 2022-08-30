from django.db import models

# Create your models here.


class Attendance(models.Model):
    id_attendance = models.AutoField(primary_key=True)
    nama_peserta = models.TextField(null=False)
    domisili_peserta = models.TextField(null=False)


class Kegiatan(models.Model):
    id_kegiatan = models.AutoField(primary_key=True)
    attendance = models.ManyToManyField(Attendance)
    nama_kegiatan = models.TextField(null=False)
    waktu_kegiatan = models.TextField(null=False)
    deskripsi = models.TextField(null=False)
