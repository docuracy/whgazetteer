# Generated by Django 2.2.10 on 2020-04-29 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_auto_20200429_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='placetype',
            name='aat_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]