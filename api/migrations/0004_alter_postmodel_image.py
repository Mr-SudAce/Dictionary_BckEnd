# Generated by Django 5.1.4 on 2024-12-20 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_postmodel_rename_word_wordmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='image',
            field=models.ImageField(default='/knowledge.png', upload_to='static/images/'),
        ),
    ]
