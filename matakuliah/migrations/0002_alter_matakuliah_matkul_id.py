# Generated by Django 4.1 on 2022-08-25 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matakuliah', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matakuliah',
            name='matkul_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
