# Generated by Django 4.0 on 2022-02-09 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='query',
        ),
        migrations.AddField(
            model_name='test',
            name='successfully',
            field=models.BooleanField(blank=True, default=1, verbose_name='Пройдено'),
            preserve_default=False,
        ),
    ]