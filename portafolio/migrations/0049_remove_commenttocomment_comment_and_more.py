# Generated by Django 4.1.5 on 2023-04-02 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0048_commenttocomment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commenttocomment',
            name='comment',
        ),
        migrations.AddField(
            model_name='commenttocomment',
            name='comment',
            field=models.ManyToManyField(to='portafolio.comment', verbose_name='comentario'),
        ),
    ]
