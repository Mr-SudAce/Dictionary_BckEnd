# Generated by Django 5.1.4 on 2025-01-02 06:44

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_rename_page_content_pagemodel_page_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagemodel',
            name='page_description',
            field=tinymce.models.HTMLField(default=''),
        ),
    ]