# Generated by Django 5.1.4 on 2024-12-20 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_alter_postmodel_description_alter_postmodel_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='image',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]