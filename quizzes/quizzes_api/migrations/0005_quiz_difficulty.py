# Generated by Django 4.2.1 on 2023-05-20 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes_api', '0004_alter_quiz_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='difficulty',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
