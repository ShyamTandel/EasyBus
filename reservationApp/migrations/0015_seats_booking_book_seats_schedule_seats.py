# Generated by Django 5.0.4 on 2024-04-30 15:55

import django.db.models.expressions
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservationApp', '0014_remove_schedule_seats_remove_booking_book_seats_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Seats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeStamp', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(default=None, null=True, on_delete=django.db.models.expressions.Case, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='book_seats',
            field=models.ManyToManyField(related_name='book_seats', to='reservationApp.seats'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='seats',
            field=models.ManyToManyField(related_name='seats', to='reservationApp.seats'),
        ),
    ]
