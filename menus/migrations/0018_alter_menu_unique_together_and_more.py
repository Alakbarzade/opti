# Generated by Django 4.0.4 on 2022-06-01 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0017_menuitem_link_parent'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='menu',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='link_parent',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='locale',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='translation_key',
        ),
    ]
