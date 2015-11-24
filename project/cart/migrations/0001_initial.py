# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20151118_2335'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='\u0434\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f \u043a\u043e\u0440\u0437\u0438\u043d\u044b')),
            ],
            options={
                'verbose_name': '\u043a\u043e\u0440\u0437\u0438\u043d\u0430',
                'verbose_name_plural': '\u041a\u043e\u0440\u0437\u0438\u043d\u044b',
            },
        ),
        migrations.CreateModel(
            name='DecalInCart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.PositiveIntegerField(verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e')),
                ('cart', models.ForeignKey(verbose_name='\u041a\u043e\u0440\u0437\u0438\u043d\u0430', to='cart.Cart')),
                ('decal', models.ForeignKey(verbose_name='\u041d\u0430\u043a\u043b\u0435\u0439\u043a\u0430', to='catalog.Decal')),
            ],
            options={
                'verbose_name': '\u044d\u043b\u0435\u043c\u0435\u043d\u0442 \u043a\u043e\u0440\u0437\u0438\u043d\u044b',
                'verbose_name_plural': '\u042d\u043b\u0435\u043c\u0435\u043d\u0442\u044b \u043a\u043e\u0440\u0437\u0438\u043d\u044b',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='\u0423\u043a\u0430\u0437\u044b\u0432\u0430\u0439\u0442\u0435 \u043f\u043e\u043b\u043d\u043e\u0441\u0442\u044c\u044e, \u043d\u0443\u0436\u043d\u043e \u0434\u043b\u044f \u0434\u043e\u0441\u0442\u0430\u0432\u043a\u0438', max_length=60, verbose_name='\u0424\u0418\u041e')),
                ('phone', models.CharField(help_text='\u041c\u044b \u043f\u043e\u0437\u0432\u043e\u043d\u0438\u043c \u0432\u0430\u043c \u0434\u043b\u044f \u0443\u0442\u043e\u0447\u043d\u0435\u043d\u0438\u044f \u0437\u0430\u043a\u0430\u0437\u0430. \u041d\u0430\u043a\u0430\u043a\u043e\u0433\u043e \u0441\u043f\u0430\u043c\u0430 \u043d\u0435 \u0431\u0443\u0434\u0435\u0442.', max_length=60, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430')),
                ('address', models.CharField(help_text='\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u0443\u043b\u0438\u0446\u0443, \u043d\u043e\u043c\u0435\u0440 \u0434\u043e\u043c\u0430 \u0438 \u043a\u0432\u0430\u0440\u0442\u0438\u0440\u0443. \u041d\u0443\u0436\u043d\u043e \u0434\u043b\u044f \u0434\u043e\u0441\u0442\u0430\u0432\u043a\u0438.', max_length=100, verbose_name='\u0410\u0434\u0440\u0435\u0441')),
                ('zip_code', models.CharField(help_text='\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u0434\u043b\u044f \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f \u043a\u043e\u043d\u0432\u0435\u0440\u0442\u0430', max_length=6, verbose_name='\u0418\u043d\u0434\u0435\u043a\u0441', blank=True)),
                ('price', models.IntegerField(verbose_name='\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c')),
                ('paid_sum', models.FloatField(null=True, verbose_name='\u041e\u043f\u043b\u0430\u0447\u0435\u043d\u043e', blank=True)),
                ('date_add', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u043e\u0444\u043e\u0440\u043c\u043b\u0435\u043d\u0438\u044f')),
                ('email', models.EmailField(help_text='\u041d\u0435 \u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u043e, \u043d\u043e \u043c\u044b \u0442\u0443\u0434\u0430 \u043f\u0440\u0438\u0448\u043b\u0435\u043c \u0434\u0430\u043d\u043d\u044b\u0435 \u043e \u0437\u0430\u043a\u0430\u0437\u0435.', max_length=254, verbose_name='Email', blank=True)),
                ('created', models.BooleanField(default=False, verbose_name='\u0418\u0437\u0433\u043e\u0442\u043e\u0432\u043b\u0435\u043d\u043e')),
                ('status', models.BooleanField(default=False, verbose_name='\u041e\u043f\u043b\u0430\u0447\u0435\u043d\u043e')),
                ('fail', models.BooleanField(default=False, verbose_name='\u0412\u0435\u0440\u043d\u0443\u043b\u043e\u0441\u044c \u043d\u0430\u0437\u0430\u0434')),
                ('sent', models.BooleanField(default=False, help_text='\u0421\u0442\u0430\u0432\u0438\u0442\u044c \u044d\u0442\u0443 \u0433\u0430\u043b\u043e\u0447\u043a\u0443 \u043a\u043e\u0433\u0434\u0430 \u043e\u0442\u043f\u0440\u0430\u0432\u0438\u043b\u0438', verbose_name='\u041e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u043e')),
                ('delivered', models.BooleanField(default=False, verbose_name='\u0414\u043e\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u043e')),
                ('received', models.BooleanField(default=False, verbose_name='\u041f\u043e\u043b\u0443\u0447\u0435\u043d\u043e')),
            ],
            options={
                'verbose_name': '\u0437\u0430\u043a\u0430\u0437',
                'verbose_name_plural': '\u0417\u0430\u043a\u0430\u0437\u044b',
            },
        ),
    ]
