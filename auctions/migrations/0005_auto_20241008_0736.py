# Generated by Django 3.1.3 on 2024-10-08 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auto_20241005_0613'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlisting',
            name='description',
            field=models.CharField(default='None', max_length=64),
        ),
        migrations.AddField(
            model_name='auctionlisting',
            name='title',
            field=models.CharField(default='New Auction', max_length=50),
        ),
    ]
