# Generated by Django 2.2.3 on 2019-08-21 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0007_bundle_is_bonus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bundle',
            name='is_bonus',
        ),
        migrations.RemoveField(
            model_name='bundle',
            name='is_published',
        ),
        migrations.RemoveField(
            model_name='bundle',
            name='quiz_for_EY',
        ),
        migrations.RemoveField(
            model_name='bundle',
            name='quiz_for_SY',
        ),
        migrations.RemoveField(
            model_name='bundle',
            name='start_date',
        ),
    ]
