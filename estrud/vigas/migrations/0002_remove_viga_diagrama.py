# Generated by Django 3.0.8 on 2020-07-06 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vigas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='viga',
            name='diagrama',
        ),
    ]
