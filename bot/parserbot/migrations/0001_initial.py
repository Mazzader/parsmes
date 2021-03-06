# Generated by Django 3.1 on 2020-08-21 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.PositiveBigIntegerField(unique=True, verbose_name="ID of user's telegram")),
                ('name', models.TextField(verbose_name="nickname of user's telegram")),
                ('score_homework_1', models.PositiveIntegerField(verbose_name='homework_1')),
                ('score_homework_2', models.PositiveIntegerField(verbose_name='homework_2')),
                ('score_homework_3', models.PositiveIntegerField(verbose_name='homework_3')),
                ('total_score', models.PositiveIntegerField(verbose_name='total_score')),
            ],
            options={
                'verbose_name': 'Profile',
            },
        ),
    ]
