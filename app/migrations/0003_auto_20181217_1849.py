# Generated by Django 2.1.4 on 2018-12-17 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20181213_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
