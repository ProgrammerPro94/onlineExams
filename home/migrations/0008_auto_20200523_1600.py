# Generated by Django 3.0.5 on 2020-05-23 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20200521_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='student',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
