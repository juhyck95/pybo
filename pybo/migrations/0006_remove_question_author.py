# Generated by Django 3.1.3 on 2021-05-31 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0005_auto_20210531_1653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='author',
        ),
    ]
