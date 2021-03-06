# Generated by Django 3.2 on 2021-09-29 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_auto_20210923_0100'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StuInfo',
        ),
        migrations.RemoveField(
            model_name='subjectsforhumanities',
            name='student',
        ),
        migrations.RemoveField(
            model_name='subjectsforscience',
            name='student',
        ),
        migrations.RemoveField(
            model_name='student',
            name='roll',
        ),
        migrations.AddField(
            model_name='student',
            name='class_roll',
            field=models.CharField(default='', max_length=6),
        ),
        migrations.AddField(
            model_name='student',
            name='ssc_roll',
            field=models.CharField(default='', max_length=6),
        ),
        migrations.AlterField(
            model_name='student',
            name='group',
            field=models.CharField(choices=[('science', 'Science'), ('humanities', 'Humanities'), ('business studies', 'Business Studies')], default='science', max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='picture',
            field=models.ImageField(blank=True, default='girl.jpeg', upload_to='student'),
        ),
        migrations.AlterField(
            model_name='student',
            name='ssc_pass_year',
            field=models.CharField(default='', max_length=4),
        ),
        migrations.DeleteModel(
            name='SubjectsForBusinessStudies',
        ),
        migrations.DeleteModel(
            name='SubjectsForHumanities',
        ),
        migrations.DeleteModel(
            name='SubjectsForScience',
        ),
    ]
