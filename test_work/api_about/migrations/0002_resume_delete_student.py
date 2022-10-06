# Generated by Django 4.1.1 on 2022-10-04 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_about', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='', max_length=30, verbose_name='Статус')),
                ('grade', models.CharField(default='', help_text='Junior, Middle, Senior, Lead', max_length=30)),
                ('specialty', models.CharField(default='', max_length=200, verbose_name='Специальность')),
                ('salary', models.FloatField(blank=True, verbose_name='Зарплата')),
                ('education', models.CharField(default='', max_length=200, verbose_name='Образование')),
                ('experience', models.TextField(verbose_name='Опыт')),
                ('portfolio', models.URLField(blank=True, help_text='Ссылка на github.com', verbose_name='Ссылка на портфолио')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254, verbose_name='Эл. адрес')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
