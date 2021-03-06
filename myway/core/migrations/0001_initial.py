# Generated by Django 3.1.2 on 2021-01-29 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(blank=True, max_length=32, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=32, null=True)),
                ('birth_date', models.DateField()),
                ('death_date', models.DateField(blank=True, null=True)),
                ('biography', models.TextField(blank=True, null=True)),
                ('events', models.ManyToManyField(to='core.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.TextField()),
                ('md5', models.CharField(max_length=32)),
                ('local', models.CharField(max_length=32)),
                ('remote', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='ShowObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('address', models.CharField(blank=True, max_length=128, null=True)),
                ('name', models.CharField(max_length=32)),
                ('events', models.ManyToManyField(to='core.Event')),
                ('persons', models.ManyToManyField(to='core.Person')),
                ('photo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.photo')),
            ],
        ),
        migrations.CreateModel(
            name='ShowPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('name', models.CharField(default='Point', max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='TripPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('name', models.CharField(default='Point', max_length=32, null=True)),
                ('order', models.IntegerField()),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='points', to='core.trip')),
            ],
        ),
        migrations.CreateModel(
            name='TripTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tag')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.trip')),
            ],
        ),
        migrations.CreateModel(
            name='TripPointObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('story', models.TextField(blank=True, null=True)),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.showobject')),
                ('trip_point', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='show_objects', to='core.trippoint')),
            ],
        ),
        migrations.CreateModel(
            name='ShowPointObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.showobject')),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.photo')),
            ],
        ),
        migrations.AddField(
            model_name='showobject',
            name='tags',
            field=models.ManyToManyField(to='core.Tag'),
        ),
        migrations.CreateModel(
            name='PersonTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.person')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tag')),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='tags',
            field=models.ManyToManyField(to='core.Tag'),
        ),
        migrations.CreateModel(
            name='EventTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.person')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tag')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='tags',
            field=models.ManyToManyField(to='core.Tag'),
        ),
        migrations.AddConstraint(
            model_name='trippointobject',
            constraint=models.UniqueConstraint(fields=('trip_point', 'object'), name='trip_point_object'),
        ),
    ]
