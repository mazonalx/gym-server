# Generated by Django 4.0.2 on 2022-02-23 18:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.URLField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
