# Generated by Django 4.1.7 on 2023-05-11 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shp', '0004_alter_deliveries_amount_deliveries_amount_of_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='amount',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shp.deliveries'),
        ),
    ]
