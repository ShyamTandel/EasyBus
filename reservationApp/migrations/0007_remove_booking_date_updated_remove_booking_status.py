# Generated by Django 4.0.3 on 2024-04-21 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservationApp', '0006_booking_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='date_updated',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='status',
        ),
    ]
