# Generated by Django 3.2 on 2021-09-30 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0004_auto_20210930_0000'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='degree_1',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='teacher',
            name='degree_2',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='teacher',
            name='degree_3',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='teacher',
            name='degree_others',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
