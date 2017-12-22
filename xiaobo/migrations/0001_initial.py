# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ops_record',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.CharField(max_length=30, verbose_name='IP\u5730\u5740')),
                ('app_id', models.CharField(max_length=10, verbose_name='\u4e1a\u52a1ID')),
                ('username', models.CharField(max_length=64, verbose_name='\u64cd\u4f5c\u7528\u6237')),
                ('result', models.CharField(max_length=256, verbose_name='\u64cd\u4f5c\u7ed3\u679c')),
            ],
            options={
                'verbose_name': '\u64cd\u4f5c\u8bb0\u5f55',
                'verbose_name_plural': '\u64cd\u4f5c\u8bb0\u5f55',
            },
        ),
    ]
