# Generated by Django 2.0 on 2020-08-18 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_postimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='country',
            field=models.CharField(default='Kenya', max_length=100),
        ),
    ]
