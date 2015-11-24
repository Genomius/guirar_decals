# coding: utf-8
from django.db import models
from catalog.models import Decal


class Cart(models.Model):
    creation_date = models.DateTimeField(u'дата создания корзины', auto_now_add=True)

    def __unicode__(self):
        return u'%s' % self.creation_date

    class Meta:
        verbose_name = u'корзина'
        verbose_name_plural = u'Корзины'


class DecalInCart(models.Model):
    cart = models.ForeignKey(Cart, verbose_name=u'Корзина')
    decal = models.ForeignKey(Decal, verbose_name=u'Наклейка')
    quantity = models.PositiveIntegerField(u'Количество')

    def __unicode__(self):
        return u'%d units of %s' % (self.quantity, self.decal)

    class Meta:
        verbose_name = u'элемент корзины'
        verbose_name_plural = u'Элементы корзины'


class Order(models.Model):
    name = models.CharField(u'ФИО', max_length=60, help_text=u'Указывайте полностью, нужно для доставки')
    phone = models.CharField(u'Номер телефона', max_length=60, help_text=u'Мы позвоним вам для уточнения заказа. Накакого спама не будет.')
    #city = models.ForeignKey(City, verbose_name=u'Город доставки')
    address = models.CharField(u'Адрес', max_length=100, help_text=u'Укажите улицу, номер дома и квартиру. Нужно для доставки.')
    zip_code = models.CharField(u'Индекс', max_length=6, blank=True, help_text=u'Укажите для создания конверта')
    price = models.IntegerField(u'Стоимость')
    paid_sum = models.FloatField(u'Оплачено', null=True, blank=True)
    date_add = models.DateTimeField(u'Дата оформления', auto_now_add=True)
    email = models.EmailField(blank=True, verbose_name=u'Email', help_text=u'Не обязательно, но мы туда пришлем данные о заказе.')

    #manager = models.ForeignKey(User, blank=True, null=True, verbose_name=u'Менеджер')
    created = models.BooleanField(default=False, verbose_name=u'Изготовлено')
    status = models.BooleanField(default=False, verbose_name=u'Оплачено')
    fail = models.BooleanField(default=False, verbose_name=u'Вернулось назад')
    sent = models.BooleanField(default=False, verbose_name=u'Отправлено', help_text=u'Ставить эту галочку когда отправили')
    delivered = models.BooleanField(default=False, verbose_name=u'Доставлено')
    received = models.BooleanField(default=False, verbose_name=u'Получено')

    #post_track_number = models.CharField(max_length=60, verbose_name=u'Почтовый трекинг номер', help_text=u'Дают на почте', blank=True, null=True)
    #payment_type = models.CharField(max_length=60, choices=PAYMENT_TYPE, verbose_name=u'Как будем платить?')

    #date_sent = models.DateTimeField(blank=True, null=True, verbose_name=u'Дата отправки', help_text=u'Ставится автоматически')

    #referral = models.ForeignKey(ReferralCode, blank=True, null=True)
    #delivery_price = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'заказ'
        verbose_name_plural = u'Заказы'
