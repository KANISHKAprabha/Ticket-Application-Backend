# Generated by Django 5.0.4 on 2024-04-24 18:08

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_image',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_description',
            field=models.TextField(blank=True, default='fill', max_length=500),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_name',
            field=models.CharField(blank=True, default='fill', max_length=500),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_start_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_venue',
            field=models.CharField(blank=True, default='fill', max_length=500),
        ),
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_name', models.CharField(blank=True, max_length=50, null=True)),
                ('max_count', models.PositiveIntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('discount_percentage', models.PositiveIntegerField()),
                ('discounted_price', models.PositiveIntegerField()),
                ('open_time_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('close_time_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('ticket_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.event')),
            ],
        ),
    ]