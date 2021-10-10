# Generated by Django 3.1.7 on 2021-03-13 19:00

import django
from django.db import migrations
from django_jsonfield_backport.models import JSONField  # noqa

import notifications.fields

django_version = float(django.get_version()[:3])

if django_version >= 3.1:
    from django.db.models import JSONField  # noqa


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_squashed_0010_notification_channels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='channels',
            field=notifications.fields.ListField(max_length=200),
        ),
        migrations.AlterField(
            model_name='notification',
            name='extra_data',
            field=JSONField(default=dict),
        ),
    ]
