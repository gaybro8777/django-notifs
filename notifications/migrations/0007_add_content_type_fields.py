# Generated by Django 2.2 on 2021-08-22 13:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('notifications', '0006_rename_obj_to_object_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='content_type',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='contenttypes.ContentType',
            ),
        ),
        migrations.AlterField(
            model_name='notification',
            name='object_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]