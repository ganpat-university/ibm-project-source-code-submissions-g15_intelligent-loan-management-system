# Generated by Django 3.0.5 on 2022-04-06 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_auto_20220406_0614'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='card_text',
            field=models.CharField(default='dummy', max_length=50),
            preserve_default=False,
        ),
    ]
