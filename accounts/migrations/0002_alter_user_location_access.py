# Generated by Django 4.0.4 on 2022-05-26 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='location_access',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
