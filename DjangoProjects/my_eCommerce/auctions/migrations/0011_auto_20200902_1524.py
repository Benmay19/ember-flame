# Generated by Django 3.0.8 on 2020-09-02 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_auctionlisting_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlisting',
            name='category',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='auctionlisting',
            name='owner',
            field=models.CharField(max_length=64),
        ),
    ]