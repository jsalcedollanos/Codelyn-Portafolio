# Generated by Django 4.1.5 on 2023-05-10 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0057_perfil_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='perfil',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='portafolio.perfil', verbose_name='perfil'),
        ),
    ]