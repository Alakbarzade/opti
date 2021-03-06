# Generated by Django 4.0.4 on 2022-06-01 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0069_log_entry_jsonfield'),
        ('menus', '0013_menu_locale_menu_translation_key_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='link_parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Parent', to='wagtailcore.page'),
        ),
    ]
