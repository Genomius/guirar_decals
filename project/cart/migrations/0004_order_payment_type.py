# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_type',
            field=models.CharField(default=123, max_length=60, verbose_name='\u041a\u0430\u043a \u0431\u0443\u0434\u0435\u043c \u043f\u043b\u0430\u0442\u0438\u0442\u044c?', choices=[(b'nal', b'\xd0\x9d\xd0\xb0\xd0\xbb\xd0\xb8\xd1\x87\xd0\xbd\xd1\x8b\xd0\xbc\xd0\xb8 \xd0\xb2 \xd0\xbc\xd0\xbe\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82 \xd0\xbf\xd0\xbe\xd0\xbb\xd1\x83\xd1\x87\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f (\xd0\xbd\xd0\xb0\xd0\xbb\xd0\xbe\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xbd\xd1\x8b\xd0\xb9 \xd0\xbf\xd0\xbb\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb6 \xd0\xbf\xd0\xbe\xd1\x87\xd1\x82\xd1\x8b \xd0\xa0\xd0\xbe\xd1\x81\xd1\x81\xd0\xb8\xd0\xb8)'), (b'internet', b'\xd0\xad\xd0\xbb\xd0\xb5\xd0\xba\xd1\x82\xd1\x80\xd0\xbe\xd0\xbd\xd0\xbd\xd1\x8b\xd0\xbc\xd0\xb8 \xd0\xb4\xd0\xb5\xd0\xbd\xd1\x8c\xd0\xb3\xd0\xb0\xd0\xbc\xd0\xb8(webmoney, \xd1\x8f\xd0\xbd\xd0\xb4\xd0\xb5\xd0\xba\xd1\x81 \xd0\xb4\xd0\xb5\xd0\xbd\xd1\x8c\xd0\xb3\xd0\xb8)'), (b'card', b'\xd0\x91\xd0\xb0\xd0\xbd\xd0\xba\xd0\xbe\xd0\xb2\xd1\x81\xd0\xba\xd0\xbe\xd0\xb9 \xd0\xba\xd0\xb0\xd1\x80\xd1\x82\xd0\xbe\xd0\xb9'), (b'mobile', b'\xd0\xa1\xd0\xbe\xd1\x82\xd0\xbe\xd0\xb2\xd1\x8b\xd0\xb5 \xd0\xbe\xd0\xbf\xd0\xb5\xd1\x80\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80\xd1\x8b'), (b'qiwi', b'\xd0\xa2\xd0\xb5\xd1\x80\xd0\xbc\xd0\xb8\xd0\xbd\xd0\xb0\xd0\xbb\xd1\x8b QIWI'), (b'alfaclick', b'\xd0\x98\xd0\xbd\xd1\x82\xd0\xb5\xd1\x80\xd0\xbd\xd0\xb5\xd1\x82 \xd0\xb1\xd0\xb0\xd0\xbd\xd0\xba \xd0\x90\xd0\xbb\xd1\x8c\xd1\x84\xd0\xb0\xd0\xba\xd0\xbb\xd0\xb8\xd0\xba')]),
            preserve_default=False,
        ),
    ]
