# Generated by Django 3.1.2 on 2021-02-28 01:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20210228_0122'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='photo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.photo'),
        ),
    ]