# Generated by Django 4.2.17 on 2024-12-24 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_alter_postmodel_postcat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='postCat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postcategory', to='api.postcategorymodel'),
        ),
    ]
