# Generated by Django 2.0.3 on 2018-03-27 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timk', '0010_game_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='slug',
            field=models.SlugField(max_length=140),
        ),
    ]
