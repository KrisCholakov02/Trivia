# Generated by Django 2.0.13 on 2019-05-19 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20190511_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileuser',
            name='city',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='profileuser',
            name='description',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='profileuser',
            name='first_name',
            field=models.CharField(blank=True, default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='profileuser',
            name='last_name',
            field=models.CharField(blank=True, default='', max_length=40),
        ),
    ]
