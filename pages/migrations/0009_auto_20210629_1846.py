# Generated by Django 3.2.3 on 2021-06-30 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_auto_20210629_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='community',
            name='topic',
            field=models.CharField(max_length=600),
        ),
    ]
