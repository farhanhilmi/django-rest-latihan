# Generated by Django 4.1 on 2022-08-27 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id_attendance', models.AutoField(primary_key=True, serialize=False)),
                ('nama_peserta', models.TextField()),
                ('domisili_peserta', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Kegiatan',
            fields=[
                ('id_kegiatan', models.AutoField(primary_key=True, serialize=False)),
                ('nama_kegiatan', models.TextField()),
                ('waktu_kegiatan', models.TextField()),
                ('deskripsi', models.TextField()),
                ('attendance', models.ManyToManyField(to='kegiatan.attendance')),
            ],
        ),
    ]
