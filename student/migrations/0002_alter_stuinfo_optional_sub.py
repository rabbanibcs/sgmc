# Generated by Django 3.2 on 2021-07-27 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stuinfo',
            name='optional_sub',
            field=models.IntegerField(),
        ),
    ]