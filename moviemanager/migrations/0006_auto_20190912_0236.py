# Generated by Django 2.2.3 on 2019-09-12 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviemanager', '0005_auto_20190911_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='time',
            field=models.CharField(max_length=20),
        ),
    ]
