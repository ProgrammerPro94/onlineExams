# Generated by Django 3.0.5 on 2020-06-01 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_question_result_teacher_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='index',
            field=models.IntegerField(default=1),
        ),
    ]
