# Generated by Django 3.0.5 on 2020-05-23 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20200523_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='student_class',
            field=models.IntegerField(default=8),
        ),
        migrations.AddField(
            model_name='result',
            name='student_section',
            field=models.CharField(default='A', max_length=1),
        ),
    ]