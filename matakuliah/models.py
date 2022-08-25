from django.db import models

# Create your models here.


class MataKuliah(models.Model):
    matkul_id = models.AutoField(primary_key=True)
    matkul_name = models.TextField(max_length=100, null=False)
    nama_dosen = models.TextField(max_length=100, null=False)
    jumlah_sks = models.IntegerField(null=False)
    ruangan = models.TextField(max_length=100, null=False)
    deskripsi = models.TextField(null=False)
    semester = models.IntegerField(null=False)
