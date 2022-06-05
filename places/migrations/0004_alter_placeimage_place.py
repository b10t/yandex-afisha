# Generated by Django 3.2.13 on 2022-06-05 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_placeimage_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placeimage',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='places.place', verbose_name='Место'),
        ),
    ]