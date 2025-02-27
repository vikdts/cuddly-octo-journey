# Generated by Django 4.2.19 on 2025-02-27 00:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('likes', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='like',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='like',
            name='content_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='like',
            name='object_id',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together={('owner', 'content_type', 'object_id')},
        ),
        migrations.RemoveField(
            model_name='like',
            name='post',
        ),
    ]
