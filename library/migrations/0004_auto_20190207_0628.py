# Generated by Django 2.1.5 on 2019-02-07 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_auto_20190207_0627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pages',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
