# Generated by Django 4.0.5 on 2022-06-01 23:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feriadomodel',
            name='tipo',
        ),
    ]
