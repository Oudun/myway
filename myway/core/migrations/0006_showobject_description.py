# Generated by Django 3.1.2 on 2021-02-01 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210130_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='showobject',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
