# Generated by Django 2.1.5 on 2019-02-06 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_auto_20190201_0820'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['full_name']},
        ),
        migrations.RenameField(
            model_name='author',
            old_name='first_name',
            new_name='full_name',
        ),
        migrations.RemoveField(
            model_name='author',
            name='last_name',
        ),
    ]