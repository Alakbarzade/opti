# Generated by Django 4.0.4 on 2022-05-30 03:38

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0069_log_entry_jsonfield'),
        ('menus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='locale',
            field=models.ForeignKey(default=1, editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailcore.locale'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menu',
            name='translation_key',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterUniqueTogether(
            name='menu',
            unique_together={('translation_key', 'locale')},
        ),
    ]



