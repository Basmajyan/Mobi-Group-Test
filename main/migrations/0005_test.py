# Generated by Django 4.0 on 2022-02-09 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_test_query'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.CharField(max_length=50, verbose_name='Сотрудник')),
                ('company', models.CharField(max_length=50, verbose_name='Компания')),
                ('date', models.DateField(auto_now=True, verbose_name='Дата')),
                ('query', models.TextField(max_length=4000, verbose_name='Вопросы (пример - 1 2 3 50 9 5 4)')),
            ],
            options={
                'verbose_name': 'Тест',
                'verbose_name_plural': 'Тесты',
            },
        ),
    ]