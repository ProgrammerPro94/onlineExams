# Generated by Django 3.0.5 on 2020-06-02 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_question_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
