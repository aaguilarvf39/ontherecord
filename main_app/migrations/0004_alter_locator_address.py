# Generated by Django 4.1 on 2022-08-17 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_locator_address_locator_name_locator_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locator',
            name='address',
            field=models.CharField(max_length=4000, null=True),
        ),
    ]
