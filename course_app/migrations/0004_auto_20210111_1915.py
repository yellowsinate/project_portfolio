# Generated by Django 3.1.5 on 2021-01-11 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0003_auto_20210111_1913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='mentor_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='student_id',
        ),
    ]
