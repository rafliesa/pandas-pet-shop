# Generated by Django 5.1.1 on 2024-09-17 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_item_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='animal_type',
            field=models.CharField(default='general', max_length=255),
            preserve_default=False,
        ),
    ]
