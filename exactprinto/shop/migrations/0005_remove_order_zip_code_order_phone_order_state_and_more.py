# Generated by Django 4.0.4 on 2022-05-18 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='Zip_code',
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='state',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='zip_code',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(default='', max_length=90),
        ),
    ]