# Generated by Django 5.1.4 on 2024-12-29 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_postcategorymodel_cat_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcategorymodel',
            name='cat_order',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]
