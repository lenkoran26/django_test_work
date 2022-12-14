# Generated by Django 4.1.2 on 2022-10-05 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_about', '0006_alter_resume_email_alter_resume_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Эл. адрес'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='experience',
            field=models.TextField(verbose_name='Опыт'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Заголовок'),
        ),
    ]
