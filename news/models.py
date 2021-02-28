#работа с бд
#CharField до 250 символов
#TextField для большого кол-ва символов
#DateTimeField для даты и времени
#DateField только для даты
from django.db import models


class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')

    def get_absolute_url(self):
        return f"/news/{self.id}"

    #Корректный вывод бд
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'



