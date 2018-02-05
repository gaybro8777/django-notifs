# Generated by Django 2.0.1 on 2018-01-28 08:27

from django.db import migrations
import notifications.fields


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0009_auto_20180112_0915'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='channels',
            field=notifications.fields.ListField(default=('console',), max_length=200),
            preserve_default=False,
        ),
    ]