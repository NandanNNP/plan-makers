# Generated by Django 3.2.4 on 2021-06-18 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_rename_user_name_payment_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='amount',
        ),
        migrations.AddField(
            model_name='payment',
            name='property_type',
            field=models.CharField(choices=[('rent_sell_house', 'rent_sell_house'), ('sell_bilding', 'sell_bilding'), ('rent_rooms', 'rent_rooms'), ('plot', 'plot')], default='rent_sell_house', max_length=20),
        ),
    ]
