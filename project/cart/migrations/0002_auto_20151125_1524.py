# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.PositiveIntegerField(verbose_name='quantity')),
                ('unit_price', models.DecimalField(verbose_name='unit price', max_digits=18, decimal_places=2)),
                ('object_id', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ('cart',),
                'verbose_name': 'item',
                'verbose_name_plural': 'items',
            },
        ),
        migrations.RemoveField(
            model_name='decalincart',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='decalincart',
            name='decal',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.AlterModelOptions(
            name='cart',
            options={'ordering': ('-creation_date',), 'verbose_name': 'cart', 'verbose_name_plural': 'carts'},
        ),
        migrations.AddField(
            model_name='cart',
            name='checked_out',
            field=models.BooleanField(default=False, verbose_name='checked out'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='creation_date',
            field=models.DateTimeField(verbose_name='creation date'),
        ),
        migrations.DeleteModel(
            name='DecalInCart',
        ),
        migrations.AddField(
            model_name='item',
            name='cart',
            field=models.ForeignKey(verbose_name='cart', to='cart.Cart'),
        ),
        migrations.AddField(
            model_name='item',
            name='content_type',
            field=models.ForeignKey(to='contenttypes.ContentType'),
        ),
    ]
