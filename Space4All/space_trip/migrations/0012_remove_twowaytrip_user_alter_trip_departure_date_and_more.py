# Generated by Django 4.0.3 on 2022-05-12 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space_trip', '0011_remove_trip_available_seats_delete_opcao_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='twowaytrip',
            name='user',
        ),
        migrations.AlterField(
            model_name='trip',
            name='departure_date',
            field=models.DateTimeField(verbose_name='departure_date'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='return_date',
            field=models.DateTimeField(verbose_name='return_date'),
        ),
        migrations.DeleteModel(
            name='OneWayTrip',
        ),
        migrations.DeleteModel(
            name='TwoWayTrip',
        ),
    ]
