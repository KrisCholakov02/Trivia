# Generated by Django 2.0.13 on 2019-05-19 11:30

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='playedgames',
            name='points',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='playedgames',
            name='number_of_questions',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(15)]),
        ),
        migrations.AlterField(
            model_name='playedgames',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
