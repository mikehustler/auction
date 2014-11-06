# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bidRecorder', '0003_auto_20141023_0533'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='auctionitem',
            name='auction',
            field=models.ForeignKey(default=1, to='bidRecorder.Auction'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registrant',
            name='auction',
            field=models.ForeignKey(default=1, to='bidRecorder.Auction'),
            preserve_default=False,
        ),
    ]
