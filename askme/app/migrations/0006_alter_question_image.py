# Generated by Django 4.2.16 on 2024-11-13 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rename_answer_count_question_answers_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, default='img/placeholder_pic.png', null=True, upload_to=''),
        ),
    ]