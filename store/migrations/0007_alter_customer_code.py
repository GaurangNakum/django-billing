# Generated by Django 3.2.5 on 2021-07-22 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='code',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
