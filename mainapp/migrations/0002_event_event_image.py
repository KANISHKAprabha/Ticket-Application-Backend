# Generated by Django 5.0.4 on 2024-04-07 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_image',
            field=models.TextField(blank=True, null=True),
        ),
    ]
