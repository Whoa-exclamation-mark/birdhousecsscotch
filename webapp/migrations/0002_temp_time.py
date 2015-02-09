# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='temp',
            name='time',
            field=models.DateTimeField(verbose_name='Time', default=datetime.datetime(2015, 2, 5, 10, 5, 28, 565084, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
