# Generated by Django 2.2.3 on 2019-08-21 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0012_remove_bundle_start_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bundle',
            name='quiz_for_EY',
        ),
        migrations.RemoveField(
            model_name='bundle',
            name='quiz_for_SY',
        ),
    ]
