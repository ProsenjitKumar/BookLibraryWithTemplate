# Generated by Django 2.1.5 on 2019-02-07 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_auto_20190207_0628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='summary',
            field=models.TextField(blank=True, help_text='Enter a brief description of the book', max_length=2000, null=True),
        ),
    ]
