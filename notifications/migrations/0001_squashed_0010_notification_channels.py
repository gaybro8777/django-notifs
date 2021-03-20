# Generated by Django 3.1.7 on 2021-03-13 18:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import notifications.fields


class Migration(migrations.Migration):

    replaces = [
        ('notifications', '0001_initial'),
        ('notifications', '0002_auto_20170718_1539'),
        ('notifications', '0003_auto_20170719_1137'),
        ('notifications', '0004_auto_20170719_1138'),
        ('notifications', '0005_auto_20170814_1118'),
        ('notifications', '0006_auto_20171005_0402'),
        ('notifications', '0007_auto_20171006_0126'),
        ('notifications', '0008_notification_extra_data'),
        ('notifications', '0009_auto_20180112_0915'),
        ('notifications', '0010_notification_channels')
    ]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),  # noqa
                ('source_display_name', models.CharField(max_length=150, null=True)),  # noqa
                ('action', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('obj', models.IntegerField(blank=True, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('is_read', models.BooleanField(default=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('short_description', models.CharField(max_length=100)),
                ('recipient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL)),  # noqa
                ('source', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),  # noqa
                ('extra_data', notifications.fields.JSONField(default={})),
                ('channels', notifications.fields.ListField(default=('console',), max_length=200)),  # noqa
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]