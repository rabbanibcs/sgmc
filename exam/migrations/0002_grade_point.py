# Generated by Django 3.2 on 2021-09-30 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='point',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]