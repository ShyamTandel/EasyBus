# Generated by Django 4.0.3 on 2024-04-21 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservationApp', '0007_remove_booking_date_updated_remove_booking_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus',
            name='isDaily',
            field=models.BooleanField(default=False),
        ),
    ]