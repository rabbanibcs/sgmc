# Generated by Django 3.2 on 2021-10-23 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0003_alter_examination_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='session',
            field=models.CharField(default=-1, max_length=9),
            preserve_default=False,
        ),
    ]
