# Generated by Django 5.1.4 on 2024-12-20 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_rename_descrption_postmodel_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='image',
            field=models.ImageField(default='images/default.jpg', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='wordmodel',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
