# Generated by Django 3.2 on 2021-10-10 11:40

import django.core.validators
from django.db import migrations, models
import student.models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0017_alter_student_admission_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileupload',
            name='admission_year',
            field=models.PositiveIntegerField(default=2021, validators=[django.core.validators.MinValueValidator(2000), student.models.max_value_current_year]),
        ),
    ]