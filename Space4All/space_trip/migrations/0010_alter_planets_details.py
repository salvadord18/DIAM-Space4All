# Generated by Django 4.0.3 on 2022-05-13 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space_trip', '0009_alter_planets_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planets',
            name='details',
            field=models.CharField(max_length=500000000000000),
        ),
    ]
