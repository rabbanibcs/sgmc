# Generated by Django 3.2 on 2021-10-19 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0022_alter_fileupload_admission_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='board',
            field=models.CharField(default='MYMENSINGH', max_length=50),
        ),
    ]
