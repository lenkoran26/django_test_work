# Generated by Django 4.1.2 on 2022-10-05 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_about', '0003_resume_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='experience',
            field=models.TextField(blank=True, verbose_name='Опыт'),
        ),
    ]
