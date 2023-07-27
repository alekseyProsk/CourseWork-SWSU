from django.db import models
from django.conf import settings
from datetime import datetime
from django.utils import dateformat
from _datetime import date


class Appeal(models.Model):
    data = models.DateField(datetime.now(), auto_now_add=True)
    theme = models.CharField('Тема обращения', max_length=100)
    textAppeal = models.TextField('Обращение')

    def __str__(self):
        return self.theme

    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'
