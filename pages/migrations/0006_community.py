# Generated by Django 3.2.3 on 2021-06-29 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20210628_1126'),
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('topic', models.TextField()),
                ('descriptions', models.TextField()),
            ],
        ),
    ]
