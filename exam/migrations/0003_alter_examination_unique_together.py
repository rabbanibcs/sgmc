# Generated by Django 3.2 on 2021-10-19 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_grade_point'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='examination',
            unique_together={('year', 'term')},
        ),
    ]
