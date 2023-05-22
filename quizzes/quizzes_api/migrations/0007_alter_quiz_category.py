# Generated by Django 4.2.1 on 2023-05-20 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes_api', '0006_remove_quiz_difficulty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_data', to='quizzes_api.category'),
        ),
    ]
