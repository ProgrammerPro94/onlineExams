# Generated by Django 3.0.5 on 2020-05-21 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_questions', models.IntegerField()),
                ('questions', models.TextField()),
            ],
        ),
    ]
