# Generated by Django 2.2.20 on 2021-06-19 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0021_placegeom_geom'),
    ]

    operations = [
        migrations.AddField(
            model_name='placegeom',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='placelink',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
