# Generated by Django 3.0.4 on 2020-03-30 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course_load', '0002_courseinstructor_course_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseAccessRequested',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_type', models.CharField(choices=[('C', 'CDC'), ('E', 'Elective')], max_length=1)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_load.Course')),
                ('department', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='course_load.Department')),
            ],
        ),
    ]