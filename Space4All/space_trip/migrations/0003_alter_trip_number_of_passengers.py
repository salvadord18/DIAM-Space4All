# Generated by Django 4.0.3 on 2022-05-12 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space_trip', '0002_trip_available_seats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='number_of_passengers',
            field=models.IntegerField(default=0),
        ),
    ]
