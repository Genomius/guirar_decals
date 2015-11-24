# coding: utf-8
from django.db import models


class Decal(models.Model):
    title = models.CharField(u'Наименование', max_length=64)
    image = models.ImageField(verbose_name=u"Изображение", upload_to="decals/")
    price = models.IntegerField(u'Цена')

    buy_count = models.IntegerField(u'Всего куплено', default=0)
    pub_date = models.DateField(u'Дата добавления', auto_now_add=True)

    slug = models.SlugField(u'URL', unique=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u"наклейка"
        verbose_name_plural = u"Наклейки"
