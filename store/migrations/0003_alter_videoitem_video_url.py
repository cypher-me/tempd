# Generated by Django 5.0.1 on 2024-01-29 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_remove_videoitem_video_file_videoitem_video_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videoitem',
            name='video_url',
            field=models.URLField(),
        ),
    ]
