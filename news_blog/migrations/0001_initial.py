# Generated by Django 2.0.1 on 2018-01-30 22:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2018, 1, 30, 22, 12, 0, 33708, tzinfo=utc))),
                ('text', models.TextField()),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
