from django.contrib.auth.models import User
from django.db import models

class Resume(models.Model):
    status = models.CharField(max_length=30, blank=False, default='', verbose_name='Статус')
    grade = models.CharField(max_length=30, blank=False, default='', help_text='Junior, Middle, Senior, Lead')
    specialty = models.CharField(max_length=200, blank=False, default='', verbose_name='Специальность')
    salary = models.FloatField(verbose_name='Зарплата', blank=True)
    education = models.CharField(max_length=200, blank=False, default='', verbose_name='Образование')
    experience = models.TextField(verbose_name='Опыт', blank=False)
    portfolio = models.URLField(verbose_name='Ссылка на портфолио', blank=True, help_text='Ссылка на github.com')
    title = models.CharField(max_length=100, blank=False, verbose_name='Заголовок')
    phone = models.CharField(max_length=20, verbose_name='Телефон', blank=False)
    email = models.EmailField(verbose_name='Эл. адрес', blank=False)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title