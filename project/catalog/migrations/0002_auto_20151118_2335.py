# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decal',
            name='buy_count',
            field=models.IntegerField(default=0, verbose_name='\u0412\u0441\u0435\u0433\u043e \u043a\u0443\u043f\u043b\u0435\u043d\u043e'),
        ),
    ]
