# Generated by Django 5.0.4 on 2024-04-25 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_alter_event_event_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_venue',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]