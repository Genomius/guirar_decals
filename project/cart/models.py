# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django_geoip.models import City


PAYMENT_TYPE = (
    ('nal', 'Оплата наличными'),
    ('card', 'Оплата картой'),
    ('internet', 'Оплата электронными деньгами'),
    ('mobile', 'Оплата с телефона'),
    ('alfaclick', 'Интернет банк Альфаклик'),
    ('qiwi', 'Терминалы QIWI'),
)

class Cart(models.Model):
    creation_date = models.DateTimeField(verbose_name=_('creation date'))
    checked_out = models.BooleanField(default=False, verbose_name=_('checked out'))

    class Meta:
        verbose_name = _('cart')
        verbose_name_plural = _('carts')
        ordering = ('-creation_date',)

    def __unicode__(self):
        return unicode(self.creation_date)


class ItemManager(models.Manager):
    def get(self, *args, **kwargs):
        if 'product' in kwargs:
            kwargs['content_type'] = ContentType.objects.get_for_model(type(kwargs['product']))
            kwargs['object_id'] = kwargs['product'].pk
            del(kwargs['product'])
        return super(ItemManager, self).get(*args, **kwargs)


class Item(models.Model):
    cart = models.ForeignKey(Cart, verbose_name=_('cart'))
    quantity = models.PositiveIntegerField(verbose_name=_('quantity'))
    unit_price = models.DecimalField(max_digits=18, decimal_places=2, verbose_name=_('unit price'))
    # product as generic relation
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()

    objects = ItemManager()

    class Meta:
        verbose_name = _('item')
        verbose_name_plural = _('items')
        ordering = ('cart',)

    def __unicode__(self):
        return u'%d units of %s' % (self.quantity, self.product.__class__.__name__)

    def total_price(self):
        return self.quantity * self.unit_price
    total_price = property(total_price)

    # product
    def get_product(self):
        return self.content_type.get_object_for_this_type(pk=self.object_id)

    def set_product(self, product):
        self.content_type = ContentType.objects.get_for_model(type(product))
        self.object_id = product.pk

    product = property(get_product, set_product)


class Order(models.Model):
    name = models.CharField(u'ФИО', max_length=60, help_text=u'Указывайте полностью, нужно для доставки')
    phone = models.CharField(u'Номер телефона', max_length=60, help_text=u'Мы позвоним вам для уточнения заказа. Накакого спама не будет.')
    city = models.ForeignKey(City, verbose_name=u'Город доставки')
    address = models.CharField(u'Адрес', max_length=100, help_text=u'Укажите улицу, номер дома и квартиру. Нужно для доставки.')
    zip_code = models.CharField(u'Индекс', max_length=6, blank=True, help_text=u'Укажите для создания конверта')
    price = models.IntegerField(u'Стоимость')
    paid_sum = models.FloatField(u'Оплачено', null=True, blank=True)
    date_add = models.DateTimeField(u'Дата оформления', auto_now_add=True)
    email = models.EmailField(blank=True, verbose_name=u'Email', help_text=u'Не обязательно, но мы туда пришлем данные о заказе.')

    created = models.BooleanField(default=False, verbose_name=u'Изготовлено')
    status = models.BooleanField(default=False, verbose_name=u'Оплачено')
    fail = models.BooleanField(default=False, verbose_name=u'Вернулось назад')
    sent = models.BooleanField(default=False, verbose_name=u'Отправлено', help_text=u'Ставить эту галочку когда отправили')
    delivered = models.BooleanField(default=False, verbose_name=u'Доставлено')
    received = models.BooleanField(default=False, verbose_name=u'Получено')

    #post_track_number = models.CharField(max_length=60, verbose_name=u'Почтовый трекинг номер', help_text=u'Дают на почте', blank=True, null=True)
    payment_type = models.CharField(max_length=60, choices=PAYMENT_TYPE, verbose_name=u'Как будем платить?')

    #date_sent = models.DateTimeField(blank=True, null=True, verbose_name=u'Дата отправки', help_text=u'Ставится автоматически')

    #referral = models.ForeignKey(ReferralCode, blank=True, null=True)
    #delivery_price = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'заказ'
        verbose_name_plural = u'Заказы'
