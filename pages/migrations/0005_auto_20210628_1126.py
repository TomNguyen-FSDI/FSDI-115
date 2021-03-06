# Generated by Django 3.2.3 on 2021-06-28 18:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_alter_post_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_on']},
        ),
        migrations.AddField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(max_length=540),
        ),
    ]
