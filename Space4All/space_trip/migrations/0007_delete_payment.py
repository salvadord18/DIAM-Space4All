# Generated by Django 4.0.3 on 2022-05-09 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('space_trip', '0006_photo_purchase_is_payed_alter_purchase_user_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
