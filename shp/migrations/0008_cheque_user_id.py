# Generated by Django 4.1.7 on 2023-06-18 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shp', '0007_cheque_image_cheque_total_price_alter_item_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='cheque',
            name='user_id',
            field=models.IntegerField(null=True),
        ),
    ]