# Generated by Django 4.0.4 on 2022-06-01 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0016_remove_menuitem_link_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='link_parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Parent', to='menus.menuitem'),
        ),
    ]
