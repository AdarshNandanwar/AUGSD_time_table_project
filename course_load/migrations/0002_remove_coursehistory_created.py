# Generated by Django 3.0.4 on 2020-11-06 02:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_load', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursehistory',
            name='created',
        ),
    ]