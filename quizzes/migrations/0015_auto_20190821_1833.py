# Generated by Django 2.2.3 on 2019-08-21 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0014_bundle_is_bonus'),
    ]

    operations = [
        migrations.AddField(
            model_name='bundle',
            name='start_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='status',
            field=models.CharField(choices=[('Ongoing', 'Ongoing'), ('Attempted', 'Attempted'), ('Try again', 'Try Again'), ('Completed', 'Completed'), ('Not submitted', 'Not Submitted')], default='Ongoing', max_length=50),
        ),
    ]
