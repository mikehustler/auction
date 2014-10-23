# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bidRecorder', '0002_auto_20141023_0325'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Person',
            new_name='Registrant',
        ),
    ]
