# Generated by Django 3.2 on 2021-10-10 11:31

import django.core.validators
from django.db import migrations, models
import student.models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0015_alter_student_class_roll'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='admission_year',
            field=models.PositiveIntegerField(default=2021, validators=[django.core.validators.MinValueValidator(1984), student.models.max_value_current_year]),
        ),
        migrations.AddField(
            model_name='student',
            name='regular',
            field=models.BooleanField(default=True),
        ),
    ]
