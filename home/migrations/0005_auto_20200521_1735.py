# Generated by Django 3.0.5 on 2020-05-21 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_test'),
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
            name='Teacher',
        ),
        migrations.DeleteModel(
            name='Test',
        ),
    ]
