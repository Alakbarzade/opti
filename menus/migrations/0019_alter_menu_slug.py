# Generated by Django 4.0.4 on 2022-06-01 15:48

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0018_alter_menu_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title', unique=True),
        ),
    ]
