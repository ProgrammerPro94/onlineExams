# Generated by Django 3.0.5 on 2020-06-03 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20200602_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='full_marks',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='result',
            name='subject',
            field=models.CharField(default='Maths', max_length=50),
        ),
    ]