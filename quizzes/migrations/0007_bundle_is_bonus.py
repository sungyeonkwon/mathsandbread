# Generated by Django 2.2.3 on 2019-08-21 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0006_auto_20190821_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='bundle',
            name='is_bonus',
            field=models.DateField(null=True),
        ),
    ]
