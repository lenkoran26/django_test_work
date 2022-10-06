# Generated by Django 4.1.1 on 2022-10-04 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='', max_length=30, verbose_name='Статус')),
                ('grade', models.CharField(default='', max_length=30)),
                ('specialty', models.CharField(default='', max_length=200, verbose_name='Специальность')),
                ('salary', models.FloatField(verbose_name='Зарплата')),
                ('education', models.CharField(default='', max_length=200, verbose_name='Образование')),
                ('experience', models.TextField(verbose_name='Опыт')),
                ('portfolio', models.URLField(verbose_name='Ссылка на портфолио')),
                ('title', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254, verbose_name='Эл. адрес')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]