# Generated by Django 4.2.13 on 2024-06-26 00:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0009_rename_usuario_users'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='Usuario',
        ),
    ]
