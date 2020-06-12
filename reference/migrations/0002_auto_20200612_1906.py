# Generated by Django 3.0.7 on 2020-06-12 12:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reference',
            options={'ordering': ('-publish',)},
        ),
        migrations.AddField(
            model_name='reference',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
