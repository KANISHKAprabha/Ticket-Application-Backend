# Generated by Django 5.0.4 on 2024-04-09 13:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_tickets_alter_event_event_end_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_group_name', models.CharField(blank=True, max_length=20, null=True)),
                ('max_count_for_group', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.RenameField(
            model_name='tickets',
            old_name='max_capacity',
            new_name='discounted_price',
        ),
        migrations.RemoveField(
            model_name='tickets',
            name='ticket_group',
        ),
        migrations.AddField(
            model_name='tickets',
            name='max_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tickets',
            name='ticket_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='mainapp.event'),
            preserve_default=False,
        ),
    ]
