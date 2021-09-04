# Generated by Django 3.2.5 on 2021-07-20 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20210720_1917'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=50)),
                ('remark', models.CharField(max_length=250)),
                ('mrp', models.IntegerField(default=0)),
                ('unit', models.CharField(max_length=10)),
                ('rate', models.IntegerField(default=0)),
                ('gst', models.IntegerField(default=0)),
                ('minq', models.IntegerField(default=0)),
                ('maxq', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='uploads/products/')),
                ('status', models.BooleanField(default=False)),
                ('cat_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.category')),
            ],
        ),
    ]