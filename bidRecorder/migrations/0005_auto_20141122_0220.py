# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bidRecorder', '0004_auto_20141105_1416'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrant',
            name='address',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.RemoveField(
            model_name='registrant',
            name='auction',
        ),
        migrations.AddField(
            model_name='registrant',
            name='city',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registrant',
            name='pc',
            field=models.CharField(default=1, max_length=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registrant',
            name='prov',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registrant',
            name='street',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='auctionitem',
            name='opening_bid',
            field=models.DecimalField(verbose_name=b'opening bid', max_digits=7, decimal_places=2),
        ),
    ]
