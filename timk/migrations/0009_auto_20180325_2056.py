# Generated by Django 2.0.3 on 2018-03-25 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timk', '0008_auto_20180325_2049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='group',
        ),
        migrations.AlterField(
            model_name='game',
            name='team1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team1', to='timk.Team'),
        ),
        migrations.AlterField(
            model_name='game',
            name='team2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team2', to='timk.Team'),
        ),
    ]
