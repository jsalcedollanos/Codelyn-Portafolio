# Generated by Django 4.1.5 on 2023-05-10 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0055_curso_aprenderas'),
    ]

    operations = [
        migrations.AddField(
            model_name='valorationcourse',
            name='star',
            field=models.IntegerField(null=True, verbose_name='estrellas'),
        ),
    ]
