# Generated by Django 4.0.6 on 2022-08-19 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autorize', '0003_quiz_result_question_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='question',
            name='quiz',
        ),
        migrations.RemoveField(
            model_name='result',
            name='quiz',
        ),
        migrations.RemoveField(
            model_name='result',
            name='user',
        ),
        migrations.DeleteModel(
            name='users',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='Quiz',
        ),
        migrations.DeleteModel(
            name='Result',
        ),
    ]
