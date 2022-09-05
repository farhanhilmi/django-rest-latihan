# Generated by Django 4.1 on 2022-09-05 02:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0002_remove_experience_experience_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExperienceType',
            fields=[
                ('experience_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('experience_name', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='experience',
            name='experience_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='experience.experiencetype'),
        ),
    ]
