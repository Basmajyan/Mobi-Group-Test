# Generated by Django 4.0 on 2022-02-09 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_test_correctanswer'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='answer6',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Ответ 6 (не обязательно)'),
        ),
        migrations.AddField(
            model_name='test',
            name='answer7',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Ответ 7 (не обязательно)'),
        ),
    ]
