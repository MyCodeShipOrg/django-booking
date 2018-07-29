# Generated by Django 2.0.7 on 2018-07-26 20:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hotelbooking', '0002_auto_20180724_0955'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='updatedAT',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='history',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='history',
            name='updatedAT',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='roomtype',
            name='services',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='history',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='History', to='hotelbooking.Room'),
        ),
    ]
