# Generated by Django 5.1.4 on 2024-12-20 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_postmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='image',
            field=models.ImageField(default='static/pi.png', upload_to='images/'),
        ),
    ]