# Generated by Django 3.0.5 on 2020-06-01 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_remove_question_test'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.RemoveField(
            model_name='test',
            name='author',
        ),
        migrations.DeleteModel(
            name='Result',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
        migrations.DeleteModel(
            name='Test',
        ),
    ]
