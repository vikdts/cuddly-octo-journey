# Generated by Django 4.2.19 on 2025-02-26 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='map_embed_code',
            field=models.TextField(blank=True, null=True),
        ),
    ]
