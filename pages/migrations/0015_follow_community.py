# Generated by Django 3.2.3 on 2021-07-01 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_post_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow_community',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default=None, max_length=200)),
                ('community_name', models.CharField(default=None, max_length=200)),
            ],
        ),
    ]
