# Generated by Django 5.1.1 on 2024-10-08 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_item_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='username',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
