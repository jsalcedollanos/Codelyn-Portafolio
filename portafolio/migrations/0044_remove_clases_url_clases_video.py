# Generated by Django 4.1.5 on 2023-02-24 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0043_alter_curso_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clases',
            name='url',
        ),
        migrations.AddField(
            model_name='clases',
            name='video',
            field=models.TextField(default='null', max_length=400),
        ),
    ]