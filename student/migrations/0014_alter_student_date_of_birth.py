# Generated by Django 3.2 on 2021-09-30 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0013_alter_student_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(blank=True, default='2000-12-01', help_text='Please use the following format: <em>YYYY-MM-DD</em>.'),
        ),
    ]
