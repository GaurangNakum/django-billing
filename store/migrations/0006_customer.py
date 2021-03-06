# Generated by Django 3.2.5 on 2021-07-21 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('code', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=250)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('contact', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
