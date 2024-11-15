# Generated by Django 5.1.3 on 2024-11-13 14:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('status', models.CharField(choices=[('DRAFT', 'Draft'), ('PUBLISHED', 'Published'), ('REJECTED', 'Rejected')], default='DRAFT', max_length=20)),
                ('category_specific_fields', models.JSONField(default=dict)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('geo_latitude', models.FloatField(blank=True, null=True)),
                ('geo_longitude', models.FloatField(blank=True, null=True)),
                ('attachments', models.ManyToManyField(related_name='reports', to='common.attachment')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.category')),
                ('tags', models.ManyToManyField(related_name='reports', to='common.tag')),
            ],
        ),
    ]
