# Generated by Django 3.2 on 2021-10-23 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0004_grade_session'),
    ]

    operations = [
        migrations.AddField(
            model_name='examination',
            name='session',
            field=models.CharField(default=-1, max_length=9),
            preserve_default=False,
        ),
    ]
