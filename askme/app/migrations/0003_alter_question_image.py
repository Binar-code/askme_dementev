# Generated by Django 4.2.16 on 2024-11-10 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_answer_correct_alter_question_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, default='static/img/placeholder_pic.png', null=True, upload_to=''),
        ),
    ]
