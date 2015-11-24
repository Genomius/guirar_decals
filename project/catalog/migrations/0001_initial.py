# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Decal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=64, verbose_name='\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435')),
                ('image', models.ImageField(upload_to=b'decals/', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435')),
                ('price', models.IntegerField(verbose_name='\u0426\u0435\u043d\u0430')),
                ('buy_count', models.IntegerField(verbose_name='\u0412\u0441\u0435\u0433\u043e \u043a\u0443\u043f\u043b\u0435\u043d\u043e')),
                ('pub_date', models.DateField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u044f')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': '\u043d\u0430\u043a\u043b\u0435\u0439\u043a\u0430',
                'verbose_name_plural': '\u041d\u0430\u043a\u043b\u0435\u0439\u043a\u0438',
            },
        ),
    ]
