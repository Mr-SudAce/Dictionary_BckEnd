# Generated by Django 5.1.4 on 2024-12-20 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_postmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='image',
            field=models.ImageField(default='/knowledge.png', upload_to='api/static/images/'),
        ),
    ]
